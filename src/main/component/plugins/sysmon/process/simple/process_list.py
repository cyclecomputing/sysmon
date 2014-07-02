from application import datastore


def setup(request, response, context):
    context.setObject("Processes", datastore.queryAds(
        "SELECT * FROM Sysmon.Process ORDER BY Cpu DESC"))
