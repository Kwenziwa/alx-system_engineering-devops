#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    base_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    data_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params_data = {
        "limit": 10
    }
    response_data = requests.get(base_url, headers=data_headers, params=params_data,
                            allow_redirects=False)
    if response_data.status_code == 404:
        print("None")
        return
    rresults_data = response_data.json().get("data")
    [print(c.get("data").get("title")) for c in rresults_data.get("children")]
