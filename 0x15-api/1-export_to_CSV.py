#!/usr/bin/python3
"""fetch information using APi"""
import requests
import sys


if __name__ == "__main__":
    API = 'https://jsonplaceholder.typicode.com/'
    todos = requests.get('{}todos?userId={}'.format(API, sys.argv[1]))
    user = requests.get('{}users/{}'.format(API, sys.argv[1]))
    username = user.json()['username']
    completed = requests.get('{}/todos?userId={}&completed=true'.format
                             (API, sys.argv[1]))

    with open('{}.csv'.format(sys.argv[1]), 'w') as csv:
        for i in todos.json():
            output = '"{}","{}","{}","{}"'.format(
                sys.argv[1], username, i['completed'], i['title'])
            csv.write(output)
            csv.write('\n')
