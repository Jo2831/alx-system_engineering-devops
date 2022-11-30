#!/usr/bin/python3
"""This python module contains a script that interacts with the Reddit API"""
import requests

def number_of_subscribers(subreddit):
    """Queries a reddit api and returns the number of subscribers for
    a given subredit"""
    header = {"User-Agent": "alx_project: josi"}
    res = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
              headers=header, allow_redirects=False)
    code = res.status_code
    return 0 if code == 404 else res.json().get("data").get("subscribers")
