#!/usr/bin/python3
"""pld"""
from requests import get, post
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = get(url)
    commits = r.json()
    counter = 0
    for commit in commits:
        if counter == 10:
            break
        print('{}: {}'.format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
        counter += 1
