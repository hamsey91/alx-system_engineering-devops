#!/usr/bin/python3
"""
Script that use this REST API for a given employee ID,
returns info about TODO list progress,using requests module.
"""

import requests
import json
import sys


if __name__ == "__main__":

    req_session = requests.Session()
    emp_id = sys.argv[1]
    url_id = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    .format(emp_id)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    emp = req_session.get(url_id)
    emp_name = req_session.get(nameURL)
    req_emp = emp.json()
    name = emp_name.json()['name']

    Tasks = 0
    for completed_tasks in req_emp:
        if completed_tasks['completed']:
            Tasks += 1
    print("Employee {} is done with tasks({}/{}):".
          format(name, Tasks, len(req_emp)))
    for completed_tasks in req_emp:
        if completed_tasks['completed']:
            print("\t " + completed_tasks.get('title'))
