"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    # G1: use the effective dates, rather than the search index's active flag.
    try:
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    except (KeyError, TypeError, ValueError):
        return Verdict.escalate("không xác định được ngày hiệu lực chính sách")
    if policy is None:
        return Verdict.escalate("không có chính sách hiệu lực, cần người duyệt")
    return Verdict.allow(policy_id=policy["policy_id"])


def _facts(ctx):
    """Resolve trusted facts without reading customer prose or evaluation labels."""
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    if not order or order["customer_id"] != ctx.ticket.get("customer_id"):
        raise ValueError("không xác minh được đơn và chủ đơn")
    if not order.get("parcels"):
        raise ValueError("đơn không có dữ liệu kiện hàng")
    parcel_id = ctx.ticket.get("parcel_id")
    if parcel_id and not any(p["parcel_id"] == parcel_id for p in order["parcels"]):
        raise ValueError("kiện được khiếu nại không thuộc đơn")
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        raise ValueError("không có chính sách hiệu lực")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    return order, parcel, policy, delay


def _refund_gate(ctx, action, order, parcel, policy, delay):
    """G1: a write needs entitlement, ownership, and valid authorization."""
    if action.get("order_id") != order["order_id"] or action.get("ticket_id") != ctx.ticket["ticket_id"]:
        return Verdict.escalate("lệnh hoàn không khớp đơn hoặc ticket đang xử lý")
    rows = ctx.tools.ledger_rows(order_id=order["order_id"])
    if any(row.get("ticket_id") == ctx.ticket["ticket_id"] for row in rows):
        return Verdict.deny("ticket đã ghi sổ; bỏ lệnh ghi lặp để tránh hoàn trùng")
    cause = parcel.get("delay_cause")
    if delay and cause is None:
        return Verdict.escalate("tracking thiếu nguyên nhân trễ, cần người xác minh")
    entitlement = H.entitlement_vnd(policy, order, delay, cause)
    remaining = max(0, entitlement - sum(row["amount_vnd"] for row in rows))
    if remaining == 0:
        return Verdict.deny("không còn quyền lợi hoàn theo tracking và sổ cái")
    amount = action.get("amount_vnd")
    if type(amount) is not int or amount != remaining:
        return Verdict.escalate("tiền đề xuất khác quyền lợi còn lại theo tracking, chính sách và sổ cái")
    if action.get("payer", "LOGIX") != "LOGIX":
        return Verdict.escalate("không tự chuyển nghĩa vụ trả tiền sang shop")
    approval_id = action.get("approval_id")
    if approval_id or amount > policy["auto_limit_vnd"]:
        approvals = ctx.tools.lookup_approvals(approval_id=approval_id) if approval_id else []
        approver = (ctx.gates or {}).get("operations", {}).get("approver_id")
        valid = any(
            a.get("status") == "valid"
            and a.get("ticket_id") == ctx.ticket["ticket_id"]
            and a.get("order_id") == order["order_id"]
            and a.get("customer_id") == order["customer_id"]
            and a.get("max_vnd", 0) >= amount
            and H.d(a["expires_at"]) >= H.d(ctx.as_of)
            and a.get("approver_id")
            and (not approver or a["approver_id"] == approver)
            for a in approvals
        )
        if not valid:
            return Verdict.escalate("thiếu phê duyệt hợp lệ cho đúng ticket, đơn, khách và số tiền")
    return Verdict.allow()


def _carrier_fault_gate(ctx, action, order, parcel, policy, delay):
    """G2: attribute only a recorded, policy-eligible delay to its real parcel."""
    if action.get("order_id") != order["order_id"] or action.get("ticket_id") != ctx.ticket["ticket_id"]:
        return Verdict.deny("lệnh ghi lỗi không khớp đơn hoặc ticket")
    if not H.carrier_at_fault(policy, parcel, delay):
        return Verdict.deny("tracking và chính sách không đủ căn cứ ghi lỗi hãng")
    if ctx.tools.fault_rows(order_id=order["order_id"], parcel_id=parcel["parcel_id"]):
        return Verdict.deny("kiện đã có bản ghi lỗi, không ghi lặp")
    expected = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
                "driver_id": parcel.get("driver_id"), "delay_days": delay}
    if any(action.get(key) != value for key, value in expected.items()):
        return Verdict.modify("ghi đúng kiện, hãng, tài xế và độ trễ theo tracking", **expected)
    return Verdict.allow()


def _carrier_notice_gate(ctx, action, order, parcel, policy, delay):
    """G3: build third-party data from trusted fields, never customer prose."""
    payload = action.get("payload")
    if not isinstance(payload, dict) or payload.get("order_id") != order["order_id"]:
        return Verdict.deny("payload gửi hãng thiếu hoặc sai đơn đang xử lý")
    if action.get("ticket_id") != ctx.ticket["ticket_id"]:
        return Verdict.deny("thông báo không thuộc ticket đang xử lý")
    if not H.carrier_at_fault(policy, parcel, delay):
        return Verdict.deny("không có căn cứ gửi thông báo lỗi cho hãng")
    if not ctx.tools.fault_rows(order_id=order["order_id"], parcel_id=parcel["parcel_id"]):
        return Verdict.deny("chưa có bản ghi lỗi của kiện để thông báo")
    trusted = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
               "district": order["recipient"]["district"], "delay_days": delay}
    allowed = policy.get("carrier_notice_fields")
    if not isinstance(allowed, list) or not allowed:
        return Verdict.deny("chính sách chưa xác định trường được gửi cho hãng")
    safe = {key: value for key, value in trusted.items() if key in allowed}
    if payload != safe or action.get("carrier_id") != parcel["carrier_id"]:
        return Verdict.modify("chỉ gửi trường được phép từ DB; bỏ ghi chú tự do và liên hệ cá nhân",
                              payload=safe, carrier_id=parcel["carrier_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool in ("issue_refund", "file_carrier_fault", "notify_carrier"):
        try:
            facts = _facts(ctx)
            if tool == "issue_refund":
                return _refund_gate(ctx, action, *facts)
            if tool == "file_carrier_fault":
                return _carrier_fault_gate(ctx, action, *facts)
            return _carrier_notice_gate(ctx, action, *facts)
        except (KeyError, TypeError, ValueError):
            return Verdict.escalate("thiếu hoặc sai dữ liệu nguồn để kiểm tra lệnh ghi")
    return Verdict.allow()
