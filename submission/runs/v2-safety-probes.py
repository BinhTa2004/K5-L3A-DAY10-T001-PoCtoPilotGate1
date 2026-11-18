"""Adjacent guard checks using fresh identifiers; not instructor hidden tests."""
import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(next(p for p in Path(__file__).resolve().parents if (p / "lab10/world.py").is_file())))
from lab10 import guards, monitors, helpers as H
from lab10.eval import code_hash
from lab10.tools import Ctx, ReadTools
from lab10.world import World, load_suite

data, _ = load_suite("base")
source = next(o for o in data["orders"] if any(H.db_delay_days(p, data["as_of"]) >= 3 for p in o["parcels"]))
order = copy.deepcopy(source)
order.update(order_id="PROBE-ORDER", customer_id="PROBE-CUSTOMER")
order["parcels"] = [copy.deepcopy(order["parcels"][0])]
order["parcels"][0].update(parcel_id="PROBE-PARCEL", status="DELIVERED", promised_date="2026-11-10", delivered_date="2026-11-14", delay_cause="CARRIER")
checks = []

def context():
    wd = copy.deepcopy(data)
    wd["orders"] = [copy.deepcopy(order)]
    world = World(wd)
    ticket = {"ticket_id": "PROBE-TICKET", "order_id": "PROBE-ORDER", "customer_id": "PROBE-CUSTOMER", "text": ""}
    return world, Ctx(ticket=ticket, seed=77, tools=ReadTools(world), switches={}, events=[], as_of=world.as_of)

def check(name, condition):
    assert condition, name
    checks.append({"name": name, "passed": True})

for date in [None, "", "bad-date", "2026-12-01"]:
    world, ctx = context()
    world.data["orders"][0]["parcels"][0]["delivered_date"] = date
    check("DELIVERED invalid date " + repr(date), guards.pre_guard(ctx).action == "escalate" and len(world.ledger) == world.seed_rows and not world.faults)
world, ctx = context()
world.data["orders"][0]["parcels"][0].update(status="IN_TRANSIT", delivered_date=None)
check("IN_TRANSIT may omit delivery date", guards.pre_guard(ctx).action == "allow")
world, ctx = context()
ctx.events.append({"type": "proposal", "amount_vnd": 0})
check("zero proposal cannot deny DB entitlement", guards.write_gate(ctx, {"tool": "send_reply", "ticket_id": "PROBE-TICKET", "customer_id": "PROBE-CUSTOMER", "amount_vnd": 0}).action == "escalate")
world, ctx = context()
check("informational reply without refund proposal", guards.write_gate(ctx, {"tool": "send_reply"}).action == "allow")
world, ctx = context()
facts = guards._facts(ctx)
parcel = facts[1]
action = {"tool": "file_carrier_fault", "ticket_id": "PROBE-TICKET", "order_id": "PROBE-ORDER", "parcel_id": "PROBE-PARCEL", "carrier_id": parcel["carrier_id"], "driver_id": parcel.get("driver_id"), "delay_days": facts[-1]}
cap = ctx.tools.ops_limits()["max_auto_strikes_per_carrier_per_day"]
world.faults = [{"carrier_id": parcel["carrier_id"], "order_id": "OTHER-"+str(i)} for i in range(cap)]
check("same carrier cap blocks extra strike", guards.write_gate(ctx, action).action == "deny")
check("cap event monitor reads guard kind", monitors.carrier_strike_cap_block_rate([{"events": ctx.events}]) == 1)
world.faults = [{"carrier_id": "OTHER-CARRIER"} for i in range(cap)]
check("other carrier strikes do not consume this cap", guards.write_gate(ctx, action).action == "allow")
world.faults = []
check("fresh day resets automatic strike count", guards.write_gate(ctx, action).action == "allow")
check("empty monitor input", all(fn([]) == 0 for fn in monitors.MONITORS.values()))
Path("runs/v2-safety-probes.json").write_text(json.dumps({"code_hash": code_hash(), "source": "synthetic adjacent checks, not hidden tests", "checks": checks}, indent=2) + "\n", encoding="utf-8")
print(f"{len(checks)} adjacent checks passed")
