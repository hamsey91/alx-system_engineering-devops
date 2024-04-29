#!/usr/bin/python3
"""
Script that use this REST API for a given employee ID,
returns info about TODO list progress,using requests module,
and export data in the JSON format.
"""

import json
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
    updateUser = {}

    for all_Emp in req_emp:
        Tasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": Uname,
            })

    updateUser[emp_id] = Tasks
    jsonFile = emp_id + ".json"
    with open(jsonFile, 'w') as f:
        json.dump(updateUser, f)
