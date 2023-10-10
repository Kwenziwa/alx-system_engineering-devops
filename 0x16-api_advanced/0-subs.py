#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response_data = requests.get(api_url, headers=headers, allow_redirects=False)
    if response_data.status_code == 404:
        return 0
    rresults_data = response_data.json().get("data")
    return rresults_data.get("subscribers")

