#!/usr/bin/python3
"""exports todo list progress to USER_ID.csv"""

if __name__ == "__main__":
    import csv
    import json
    import requests
    from sys import argv

    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')\
        .json()
    user_dict = {}
    for user in requests.get('https://jsonplaceholder.typicode.com/users')\
            .json():
        user_dict[user.get('id')] = user.get('username')

    data = {}
    for user_id, username in user_dict.items():
        task_list = []
        for todo in todo_list:
            task_dict = {}
            task_dict['task'] = todo.get('title')
            task_dict['completed'] = todo.get('completed')
            task_dict['username'] = username
            task_list.append(task_dict)
        data = {user_id: task_list}

    with open('todo_all_employees.json', 'w', encoding='UTF8') as f:
        json.dump(data, f)
