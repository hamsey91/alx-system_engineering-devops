#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":

    Users_req = requests.get("https://jsonplaceholder.typicode.com/users")
    Users_json = users.json()
    Todos_req = requests.get('https://jsonplaceholder.typicode.com/todos')
    Todos_json = todos.json()
    All_Todos = {}

    for User in Users_json:
        List_Tasks = []
        for Task in Todos_json:
            if Task.get('userId') == User.get('id'):
                Dic_Tasks = {"username": User.get('username'),
                            "task": Task.get('title'),
                            "completed": Task.get('completed')}
                List_Tasks.append(Dic_Tasks)
        All_Todos[User.get('id')] = List_Tasks

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(All_Todos, f)
