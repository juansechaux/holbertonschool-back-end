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

    # employee_id = str(argv[1])

    users_url = "https://jsonplaceholder.typicode.com/users/"

    users_response = requests.get(users_url)

    if users_response.status_code == 200:
        users_data = users_response.json()
        # user_name = users_data.get("username")  # username of the user

    todos_url = "https://jsonplaceholder.typicode.com/todos/"

    todos_response = requests.get(todos_url)

    if todos_response.status_code == 200:
        todos_data = todos_response.json()
        return_dict = {}
        for user_dict in users_data:
            list_of_dicts = []
            user_id = user_dict.get("id")
            user_name = user_dict.get("username")
            for dict in todos_data:
                dict_task = {}
                if dict.get("userId") == user_id:
                    dict_task['username'] = user_name
                    dict_task['task'] = (dict.get("title"))
                    dict_task['completed'] = (dict.get("completed"))
                    list_of_dicts.append(dict_task)
            return_dict[user_id] = list_of_dicts
        with open("todo_all_employees.json", 'w', newline='') as json_file:
            json.dump(return_dict, json_file)
        # print(return_dict.keys())


if __name__ == "__main__":

    display_info()
