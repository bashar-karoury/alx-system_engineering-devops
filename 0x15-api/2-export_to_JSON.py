#!/usr/bin/python3
""" Module to exprot info about TODOs of user id from API into JSON file
"""
import json
import requests
import sys
if __name__ == "__main__":
    if sys.argv[1]:
        id = sys.argv[1]
        # get name of userid
        usersUrl = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        userInfo = requests.get(usersUrl).json()
        userName = userInfo.get("username")
        url = "https://jsonplaceholder.typicode.com/todos"
        response = requests.get(url)
        # print("status code ", response.status_code)
        todos = response.json()
        tasks = []
        for todo in todos:
            if todo.get('userId') == int(id):
                tasks.append({
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": userName})
        data = {id: tasks}
        print(data)
        # write to file
        with open('{}.json'.format(id), mode='w', newline='') as file:
            json.dump(data, file)
