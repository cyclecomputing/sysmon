from application import datastore, logger, expressions
from apex import adserializer
from sysmonlib import process


def run(timer):
    result = process.monitor()

    datastore.synchronizeAds(result, 
        expressions.parse("AdType == \"Sysmon.Process\""))

    logger.info("Stored %s process samples" % len(result))


def get(request, response):
    response.write(adserializer.serializeToString(process.monitor(), 'text'))
