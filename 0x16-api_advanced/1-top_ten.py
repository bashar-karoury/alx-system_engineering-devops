#!/usr/bin/python3
""" module which contains a function that queries top ten hot
    post of subreddit
"""
import requests


def top_ten(subreddit):
    """ returns top ten hot posts for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        titles = []
        for child in children:
            titles.append(child['data']['title'])
            print(titles[-1])
        return titles
    else:
        return None
