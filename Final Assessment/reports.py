#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Table, Image

directory = "/home/student-03-b60bd46ecaa6/supplier-data/descriptions/"

def generate_report(attachment, title, paragraph):
        report = SimpleDocTemplate(attachment)
        report_title = title
        report_body = Paragraph(paragraph)
        report.build([report_title, report_body])
