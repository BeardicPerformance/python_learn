#!/usr/bin/env python3

import requests
import os

directory = "/home/student-03-b60bd46ecaa6/supplier-data/images/"
url = "http://localhost/upload/"
for img in os.listdir(directory):
        if img[3:] == ".jpeg":
                print("uploading {}".format(img))
                with open("/home/student-03-b60bd46ecaa6/supplier-data/images/{}".format(img), "rb") as image:
                        r = requests.post(url, files={"file": image})
        else:
                print("skipping {}".format(img))

