# -*- coding: utf-8 -*-
def recursive_function(parameters):
    import time
    count = parameters
    if parameters > 0:
        print(count)
        time.sleep(1)
        recursive_function(count-1)
    elif parameters == 0:
        print("LIFT OFF")

    
recursive_function(10)