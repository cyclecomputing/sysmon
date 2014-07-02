import subprocess
from application import logger
from com.cyclecomputing.apex.ad import Ad


def parse_int(input):
    return int(input)


def parse_percent(input):
    return float(input) / 100


properties = ["pid", "user", "rss", "vsz", "pcpu", "ucomm", "command"]

propertiesMap = {
    "pid": "PID",
    "user": "User",
    "rss": "ResidentSize",
    "vsz": "VirtualSize",
    "pcpu": "CPU",
    "ucomm": "Name",
    "command": "Command"
}

parseMap = {
    "pid": parse_int,
    "rss": parse_int,
    "vsz": parse_int,
    "pcpu": parse_percent,
}


def monitor():
    '''
    Run a 'ps' command and return Sysmon.Process records
    '''
    cmd = ["/bin/ps", "axww", "-o", ",".join(properties)]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    logger.info("Running ps command: %s" % " ".join(cmd))

    return parse(p.communicate()[0])


def kill(pid):
    '''
    Kill a process by PID
    '''
    p = subprocess.Popen(\
        ["/bin/kill", str(pid)],\
        stdout=subprocess.PIPE)
    return p.communicate()


def parse(contents):
    '''
    Parse the output of the 'ps' command and return a list of records
    '''
    lineNo = 0
    processes = []
    for line in contents.split("\n"):
        line = line.strip()

        lineNo = lineNo + 1
        if lineNo == 1 or len(line) == 0:
            continue

        parts = line.split(None, len(properties) - 1)

        process = Ad("Sysmon.Process")
        for n in range(len(parts)):
            part = parts[n]
            property = properties[n]
            attribute = propertiesMap[property]

            value = part
            if property in parseMap:
                value = parseMap[property](part)

            process.setObject(attribute, value)

        processes.append(process)

    logger.info("Parsed %d processes" % len(processes))

    return processes
