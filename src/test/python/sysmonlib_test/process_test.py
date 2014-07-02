import plugintest
import os
from sysmonlib import process


class Test(plugintest.TestCase):

    def test_parse(self):
        f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),\
            "ps_output.txt"), 'r')
        processes = process.parse(f.read())

        # 139 Processes Parsed
        self.assertEquals(186, len(processes))

        # Spot check some individual processes
        p = processes[0]
        self.assertEquals(1, p.getAsInteger("PID"))
        self.assertEquals("root", p.getAsString("User"))

        p = processes[165]
        self.assertEquals(6809, p.getAsInteger("PID"))
        self.assertEquals("ganglia", p.getAsString("User"))
        self.assertEquals("/opt/ganglia/current/sbin/gmetad", p.getAsString("Command"))
