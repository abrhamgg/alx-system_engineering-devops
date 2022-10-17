#!/usr/bin/python3
"""fetch information using APi"""
import requests
import sys

if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/'
                         'todos?userId={}'.format(sys.argv[1]))
    user = requests.get('https://jsonplaceholder.typicode.com/'
                        'users/{}'.format(sys.argv[1]))
    completed = requests.get('https://jsonplaceholder.typicode.com'
                             '/todos?userId={}&completed=true'.format
                             (sys.argv[1]))
    EMPLOYEE_NAME = user.json()['name']
    NUMBER_OF_DONE_TASKS = len(completed.json())
    TOTAL_NUMBER_OF_TASKS = len(todos.json())

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in completed.json():
        print("\t {}".format(i['title']))
