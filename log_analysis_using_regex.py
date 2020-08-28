# -*- coding: utf-8 -*-
#!/bin/usr/env python3
"""
Created on Tue Aug 25 14:36:08 2020

@author: Jonathan
"""
import re
import sys
import csv

per_user = {}
error = {}

def get_dict(logfile):
    regex = r"ticky: ([A-Z]+): (.*) \((.*)\)"
    with open(logfile) as f:
        for line in f.readlines():
            result = re.search(regex, line)
            if result[1] == "ERROR":
                if not result[3] in per_user:
                    per_user[result[3]] = ["ERROR"]
                else:
                    per_user[result[3]] += ["ERROR"]
                if not result[2] in error:
                    error[result[2]] = 1
                else:
                    error[result[2]] += 1
            elif result[1] == "INFO":
                if not result[3] in per_user:
                    per_user[result[3]] = ["INFO"]
                else:
                    per_user[result[3]] += ["INFO"]
            else:
                raise TypeError("{} does not contain required value".format(line))
    for user, li in per_user.items():
        errors = li.count("ERROR")
        infos = li.count("INFO")
        per_user[user] = [infos,errors]

def export_user_csv(d):
    with open('user_statistics.csv', 'w') as csv_file:
        fieldnames = ['Username', "INFO", "ERROR"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for user, li in sorted(d.items()):
            writer.writerow({"Username": user, "INFO": li[0], "ERROR": li[1]})

def export_error_csv(d):
    with open('error_message.csv', 'w') as csv_file:
        fieldnames = ["Error", "Count"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for err,count in sorted(d.items(), key=lambda item: item[1]):
            writer.writerow({"Error": err, "Count": count})



get_dict("C:/python_learn/syslog.log")
export_user_csv(per_user)
export_error_csv(error)
