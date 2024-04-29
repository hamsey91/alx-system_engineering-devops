#!/usr/bin/python3
"""
Script that use this REST API for a given employee ID,
returns info about TODO list progress,using requests module,
and export data in the CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":

    req_session = requests.Session()
    emp_id = sys.argv[1]
    url_id = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    nameURL = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    emp = req_session.get(url_id)
    emp_name = req_session.get(nameURL)
    req_emp = emp.json()
    Uname = emp_name.json()['username']

    Tasks = 0
    for completed_tasks in req_emp:
        if completed_tasks['completed']:
            Tasks += 1

    fileCSV = emp_id + '.csv'
    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in req_emp:
            write.writerow([emp_id, Uname, i.get('completed'), i.get('title')])