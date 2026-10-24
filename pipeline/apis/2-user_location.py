#!/usr/bin/python3
"""Get the location of a GitHub user using the GitHub API."""

import requests
import sys
import time
import math


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        print(response.json().get('location'))

    elif response.status_code == 404:
        print("Not found")

    elif response.status_code == 403:
        reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
        minutes = math.ceil((reset_time - time.time()) / 60)
        print("Reset in {} min".format(max(0, minutes)))
