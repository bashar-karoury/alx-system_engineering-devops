#!/usr/bin/python3
""" Module to get info about TODOs of user id from API
"""
import sys
import requests
if sys.argv[1]:
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    # print("status code ", response.status_code)
    todos = response.json()
    completed = []
    tasks_cout = 0
    for todo in todos:
        if todo.get('userId') == int(id):
            tasks_cout += 1
            if todo.get("completed") is True:
                completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
                                            id, len(completed), tasks_cout))
    for item in completed:
        print("\t", item)
