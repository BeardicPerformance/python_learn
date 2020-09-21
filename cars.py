#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}
  sales_by_year = {}
  max_year = 0
  max_year_sales = 0
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    item_sales = item["total_sales"]
    if item_sales > max_sales["total_sales"]:
      max_sales = item
    # TODO: also handle most popular car_year
    item_car = item["car"]
    item_year = item_car["car_year"]
    if item_year in sales_by_year:
      sales_by_year[item_year] += item_sales
    elif item_year not in sales_by_year:
      sales_by_year[item_year] = item_sales
  for key, value in sales_by_year.items():
    if value > max_year_sales:
      max_year_sales = value
      max_year = key

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(
      format_car(max_sales["car"]), max_sales["total_sales"]),
    "The most popular year was {} with {} sales".format(
      max_year, max_year_sales)
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("/home/student-03-1fd9fe7bcaed/car_sales.json")
  summary = process_data(data)
  table_data = cars_dict_to_table(data)
  print(summary)
  # TODO: turn this into a PDF report
  pdf_summary = "{}<br/>{}<br/>{}".format(summary[0],summary[1],summary[2])
  reports.generate("/tmp/cars.pdf","Car Sales",pdf_summary,table_data)
  # TODO: send the PDF report as an email attachment
  email_body = "{}\n{}\n{}".format(summary[0],summary[1],summary[2])
  message = emails.generate("automation@example.com","student-03-1fd9fe7bcaed@example.com","Sales summary for last month",email_body,"/tmp/cars.pdf")
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)


