from application import datastore
from sysmonlib import process

PROC_TYPE = "Sysmon.Process"


def execute(cmd):
    action = cmd.getAsString("Action")
    procs = datastore.findAdsByType(PROC_TYPE, cmd.getAsExpression("Filter"))
    if action == "Sysmon.Process.Kill":
        for p in procs:
            pid = p.getAsInteger("PID")
            if pid:
                process.kill(pid)
