#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

directory = "/home/student-03-b60bd46ecaa6/supplier-data/descriptions/"
fruits = []
paragraph = ""
for file in os.listdir(directory):
        content = []
        f = open("/home/student-03-b60bd46ecaa6/supplier-data/descriptions/{}".format(file))
        lines = f.readlines()
        for line in lines:
                line = line.rstrip()
                content.append(line)
        fruit = {"name":content[0], "weight":content[1]}
        fruits.append(fruit)
for fruit in fruits:
        for name, weight in fruit.items():
                paragraph += "name: {}/n weight: {}/n /n".format(name,weight)

title = "Processed Update on {}".format(date.today())
attachment = "/tmp/processed.pdf"
sender = "automation@example.com"
recipient = "student-03-b60bd46ecaa6@example.com"
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

if __name__ == "__main__":
        reports.generate_report(attachment, title, paragraph)
        message = emails.generate_email(sender,recipient,subject,body,attachment)
        emails.send_email(sender,recipient,message)

