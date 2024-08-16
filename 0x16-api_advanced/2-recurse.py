#!/usr/bin/python3
""" module which contains a function returns all titles of hot
    posts of subreddit,None if subreddit is invalid
"""
import requests


def recurse(subreddit, hot_list=[], after="NULL"):
    """ returns all titles of hot posts of subreddit,
        None if subreddit is invalid
    """
    if after is None:
        print(len(hot_list))
        return hot_list
    headers = {'User-Agent': 'alx/1.0'}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
                                                    subreddit, after)
    response = requests.get(url, allow_redirects=False, headers=headers)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        after = data['data']['after']
        for child in children:
            hot_list.append(child['data']['title'])
        return recurse(subreddit, hot_list, after=after)
    else:
        return None
