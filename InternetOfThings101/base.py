#!/usr/bin/env python

import signal
import sys
import time

def functionSignalHandler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, functionSignalHandler)

    while True:
        print "Hello Internet of Things 101"
        time.sleep(5)

# End of File
