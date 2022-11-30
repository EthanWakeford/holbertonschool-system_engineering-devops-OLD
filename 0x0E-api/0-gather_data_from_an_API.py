#!/usr/bin/python3
"""returns info about TODO list progress for user with fake api"""
if __name__ == "__main__":
    import requests
    from sys import argv

    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')\
        .json()
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()['name']
    task_dict = {}
    for todo in todo_list:
        if todo.get('userId') == int(argv[1]):
            task_dict[todo.get('title')] = todo.get('completed')
    print('Employee {} is done with tasks({}/{}):'
          .format(name, sum(task_dict.values()), len(task_dict)))

    for key, value in task_dict.items():
        if value is True:
            print('\t {}'.format(key))
