#!/usr/bin/python3
""" module which contains a function that queries the Reddit API and
    returns the number of subscribers
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ eturns the number of subscribers (not active users,
        total subscribers) for a given subreddit
    """
    # URL with parameters
    # print(sys.argv[1])
    url = 'https://www.reddit.com/r/{}/about.json'.format(sys.argv[1])

    # Query parameters
    # params = {'key1': 'value1', 'key2': 'value2'}

    # Custom headers
    # headers = {'Authorization': 'Bearer your_token_here'}
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        data = data['data']
        return data['subscribers']
    else:
        return 0
