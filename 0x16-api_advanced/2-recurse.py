#!/usr/bin/python3
"""Module allows you to send HTTP requests using Python"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after) if after else "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozila/5.0'}
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
        recurse(subreddit, hot_list, after=after)
    return hot_list
