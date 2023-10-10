#!/usr/bin/python3
"""
Using reddit's API
"""
import requests
after_para = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    global after_para
    user_headers = {'User-Agent': 'api_advanced-project'}
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    paras = {'after': after_para}
    data_resuts = requests.get(base_url, params=paras, headers=user_headers,
                           allow_redirects=False)

    if data_resuts.status_code == 200:
        after_data = data_resuts.json().get("data").get("after")
        if after_data is not None:
            after_para = after_data
            recurse(subreddit, hot_list)
        titles_all_data = data_resuts.json().get("data").get("children")
        for title_ in titles_all_data:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
