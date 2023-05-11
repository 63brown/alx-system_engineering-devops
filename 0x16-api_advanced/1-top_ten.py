#!/usr/bin/python3
"""Module allows you to send HTTP requests using Python"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts[:10]:
        title = post['data']['title']
        print(title)
