#!/usr/bin/env python3

import PIL
import os
from pathlib import Path
from PIL import Image

directory = "/home/student-03-44dc6185a974/images"

def image_fix(img):
        with Image.open(img) as img:
                new_img = img.rotate(90).resize((128,128)).convert("RGB")
                new_img.save("/opt/icons/{}.jpeg".format(img.filename))

for img in os.listdir(directory):
        if img !=  "image_fix.py":
                image_fix(img)



