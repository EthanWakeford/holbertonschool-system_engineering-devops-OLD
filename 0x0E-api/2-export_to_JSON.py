#!/usr/bin/python3
"""exports todo list progress to USER_ID.csv"""

if __name__ == "__main__":
    import csv
    import json
    import requests
    from sys import argv

    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')\
        .json()
    username = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1])).json().get('username')
    task_list = []
    for todo in todo_list:
        task_dict = {}
        task_dict['task'] = todo.get('title')
        task_dict['completed'] = todo.get('completed')
        task_dict['username'] = username
        task_list.append(task_dict)

    data = {'{}'.format(argv[1]): task_list}

    with open('{}.json'.format(argv[1]), 'w', encoding='UTF8') as f:
        json.dump(data, f)
