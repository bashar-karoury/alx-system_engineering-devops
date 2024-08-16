#!/usr/bin/python3
""" module which contains a function that queries
    the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ eturns the number of subscribers (not active users,
        total subscribers) for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        data = data['data']
        return data['subscribers']
    else:
        return 0
