#!/usr/bin/python3
"""Module allows you to send HTTP requests using Python"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            if word.lower() in title:
                if word.lower() not in count_dict:
                    count_dict[word.lower()] = 1
                else:
                    count_dict[word.lower()] += 1
    if not data['data']['after']:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for count in sorted_counts:
            print(count[0], ':', count[1])
        return
    else:
        return count_words(subreddit, word_list, data['data']['after'], count_dict)
