# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:19:52 2020

@author: Jonathan
"""
# enter name closed in parentheses like ["Jon Olson", "robertson", "batson"]
list_name = ["Willard Johnson", "Robertson", "Jo smith"]
# enter DAPPS ID closed in parentheses like ["daam558694", "daah768966", "batso303"]
list_dapps = ["dabh775865", "daah768966", "dafg785265"]

def def_pass(name,dapps):
    from datetime import date
    new_name=name.lower()
    li = list(new_name.split(" "))
    new_name = li[-1]
    today = str(date.today())
    print("Temp password for " + name + ", " + dapps + ", is: " + str("N"+today[-5:-3]+today[-2:]+dapps[-2:]+new_name[0]))
    
for name in  list_name:
    dapps = list_dapps.pop(0)
    def_pass(name,dapps)

