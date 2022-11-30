#!/usr/bin/python3
"""exports todo list progress to USER_ID.csv"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')\
        .json()
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json().get('name')
    task_dict = {}
    for todo in todo_list:
        if todo.get('userId') == int(argv[1]):
            task_dict[todo.get('title')] = todo.get('completed')

    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as f:
        for task_title, completed_status in task_dict.items():
            writer = csv.writer(f,  quoting=csv.QUOTE_ALL)
            writer.writerow([argv[1], name, completed_status, task_title])
