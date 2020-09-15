#!/usr/bin/env python3

import PIL
import os
from pathlib import Path
from PIL import Image

directory = "/home/student-03-b60bd46ecaa6/supplier-data/images/"

def image_fix(img):
        filename = img[0:3]
        with Image.open("/home/student-03-b60bd46ecaa6/supplier-data/images/{}".format(img)) as image:
                new_img = image.resize((600,400)).convert("RGB")
                new_img.save("/home/student-03-b60bd46ecaa6/supplier-data/images/{}.jpeg".format(filename))

for img in os.listdir(directory):
        if img[3:] == ".tiff":
                print("fixing {}".format(img))
                image_fix(img)
        else:
                print("skipping {}".format(img))

