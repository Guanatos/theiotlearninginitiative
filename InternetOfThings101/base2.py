#!/usr/bin/env python

#import psutil
from random import randint

import signal
import sys
import time

def functionDataSensor():
#    netdata = psutil.net_io_counters()
#    data = netdata.packets_sent + netdata.packets_recv
    data = randint(0,100)
    return data

def functionSignalHandler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, functionSignalHandler)

    while True:
        print "Hello Internet of Things 101"
        print "Data Sensor: %s " % functionDataSensor()
        time.sleep(5)

# End of File
