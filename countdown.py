#!/usr/bin/env python3

import sys
import time

def recursive_function(parameters):
    parameters = int(parameters)
    count = parameters
    if parameters < 0:
        print("ERROR: Invalid parameters!")
    elif parameters > 0:
        print(count)
        time.sleep(1)
        recursive_function(count-1)
    elif parameters == 0:
        print("LIFT OFF")


recursive_function(sys.argv[1])
