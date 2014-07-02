from application import datastore


def setup(request, response, context):
    try:
        pid = int(request.attribute("pid"))
    except:
        pid = None

    if pid:
        result = datastore.queryAds(
            "SELECT * FROM Sysmon.Process WHERE PID === %d" % pid)
        if len(result) > 0:
            context.setAd("Process", result[0])
