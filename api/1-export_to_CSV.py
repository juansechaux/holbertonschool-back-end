#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress.
"""
import csv
import requests
from sys import argv


def display_info():
    '''
    This is the function to serch for a user info and tasks.
    '''

    employee_id = str(argv[1])

    users_url = "https://jsonplaceholder.typicode.com/users/" + employee_id

    users_response = requests.get(users_url)

    if users_response.status_code == 200:
        users_data = users_response.json()
        user_name = users_data.get("username")  # username of the user

    todos_url = "https://jsonplaceholder.typicode.com/todos/"

    todos_response = requests.get(todos_url)

    if todos_response.status_code == 200:
        todos_data = todos_response.json()
        dict_task = {}
        for dict in todos_data:
            if dict.get("userId") == int(employee_id):
                dict_task['id'] = employee_id
                dict_task['username'] = user_name
                dict_task['completed'] = (dict.get("completed"))
                dict_task['title'] = (dict.get("title"))
                with open(str(employee_id) + ".csv", 'a',
                          newline='') as archivo_csv:
                    writer = csv.writer(archivo_csv, quoting=csv.QUOTE_ALL)
                    writer.writerow(dict_task.values())


if __name__ == "__main__":

    display_info()
