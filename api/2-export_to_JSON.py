#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress.
"""
import csv
import json
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
        list_of_dicts = []
        return_dict = {}
        for dict in todos_data:
            dict_task = {}
            if dict.get("userId") == int(employee_id):
                dict_task['task'] = (dict.get("title"))
                dict_task['completed'] = (dict.get("completed"))
                dict_task['username'] = user_name
                list_of_dicts.append(dict_task)
        return_dict[employee_id] = list_of_dicts
        with open(str(employee_id) + ".json", 'a', newline='') as json_file:
            json.dump(return_dict, json_file)
        # print(return_dict)


if __name__ == "__main__":

    display_info()
