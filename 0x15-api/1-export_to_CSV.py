#!/usr/bin/python3
""" Module to exprot info about TODOs of user id from API into csv file
"""
import csv
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
                tasks.append([id, userName, todo.get("completed"), todo.get(
                                                                    "title")])
        # write to file
        with open('{}.csv'.format(id), mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)

            # Write the data row by row
            for task in tasks:
                writer.writerow(task)
