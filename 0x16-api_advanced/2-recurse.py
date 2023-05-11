#!/usr/bin/python3
"""Module allows you to send HTTP requests using Python"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)

    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title']
        hot_list.append(title)

    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after=after)

    return hot_list
