# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:04:21 2020

@author: Jonathan
"""

def create_python_script(filename):
  comments = "# Start of a new Python program"
  import os
  with open(filename, 'w+') as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))