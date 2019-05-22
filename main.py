import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    base_url = 'https://api.github.com'
    url = base_url + f'/users/{username}/events/public'
    response = requests.get(url)
    print(response.json()[0]['created_at'])





