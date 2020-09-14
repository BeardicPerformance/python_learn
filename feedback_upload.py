#!/usr/bin/env python3

import os
import requests

reviews = []
files = os.listdir("/data/feedback")
for file in files:
        content = []
        f = open("/data/feedback/{}".format(file))
        lines = f.readlines()
        for line in lines:
                line = line.rstrip()
                content.append(line)
        review = {"title" : content[0], "name" : content[1], "date" : content[2], "feedback" : content[3]}
        reviews.append(review)
for review in reviews:
        response = requests.post("http://34.72.115.93/feedback/", json=review)
        print(review)
        response.raise_for_status()

