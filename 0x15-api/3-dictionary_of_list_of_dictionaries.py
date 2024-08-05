#!/usr/bin/python3
""" Module to exprot info about TODOs of all users from API into JSON file
"""
import json
import requests


def appendToListOfDict(dictionary, key, value):
    """ Append a value to list of a key in dictionary and initialize it if not
        exist
    """
    if not dictionary.get(key):
        dictionary[key] = []
    dictionary[key].append(value)


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    # print("status code ", response.status_code)
    todos = response.json()
    data = {}
    users = {}
    for todo in todos:
        # get userId so we can get request for userName
        userId = str(todo.get('userId'))
        userName = users.get(userId)
        if not userName:
            # get name of userid
            usersUrl = "https://jsonplaceholder.typicode.com/users/{}".format(
                                                                        userId)
            userInfo = requests.get(usersUrl).json()
            userName = userInfo.get("username")
            # save to dict users
            users[id] = userName
        appendToListOfDict(data, userId, {
                            "task": todo.get("title"),
                            "completed": todo.get("completed"),
                            "username": userName})
    # write to file
    with open('todo_all_employees.json', mode='w', newline='') as file:
        json.dump(data, file)
