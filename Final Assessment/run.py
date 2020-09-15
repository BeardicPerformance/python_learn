#!/usr/bin/env python3

import os
import requests
import re

directory = "/home/student-03-b60bd46ecaa6/supplier-data/descriptions/"
fruits = []
for file in os.listdir(directory):
        content = []
        f = open("/home/student-03-b60bd46ecaa6/supplier-data/descriptions/{}".format(file))
        lines = f.readlines()
        for line in lines:
                line = line.rstrip()
                content.append(line)
        weight = re.sub('[^0-9]','',content[1])
        fruit = {"name":content[0], "weight":int(weight), "description":content[2], "image_name":"{}.jpeg".format(file[0:3])}
        fruits.append(fruit)
for fruit in fruits:
        response = requests.post("http://34.69.148.85/fruits/", json=fruit)
        print(fruit)
        response.raise_for_status()


