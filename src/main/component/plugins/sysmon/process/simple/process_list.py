from application import datastore


def setup(request, response, context):
    context.setObject("Processes", datastore.query(
        "SELECT * FROM Sysmon.Process ORDER BY Cpu DESC"))
