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
        return hot_list

    headers = {'User-Agent': 'bashar_alx/1.0'}
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
        print("invalid", response.status_code)
        return None


def count_words(subreddit, word_list):
    """ queries the Reddit API, parses the title of all hot articles
        , and prints a sorted count of given keywords
    """
    count_dict = {}
    hot_list = recurse(subreddit)
    if not hot_list:
        return None

    for word in word_list:
        for hot in hot_list:
            if word.lower() in hot:
                if not count_dict.get(word.lower()):
                    count_dict[word.lower()] = 1
                else:
                    count_dict[word.lower()] += 1

    # Sort by count (descending) and then alphabetically by word (ascending)
    count_list = sorted(
        count_dict.items(), key=lambda item: (-item[1], item[0]))
    for word, count in count_list:
        print("{}: {}".format(word, count))
    return count_list
