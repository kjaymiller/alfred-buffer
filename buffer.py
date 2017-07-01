#!/usr/local/bin/python3
"""
Capture your text in quotes and make it the final argument
Add the profile IDs of your choice

Possible Improvements:
 * Find a way to select multiple accounts at once so this isn't necessary
 * Select the first account as the default and let people know
"""

import requests
from sys import argv

text = text_formatted = argv[-1]
# You will need to register your app to get this token https://buffer.com/developers/apps/create
token = '<YOUR BUFFER TOKEN>'

url = f'https://api.bufferapp.com/1/updates/create.json?access_token={token}'
profile_ids = [x for x in argv[1:-1]]
for profile in profile_ids:
    data = {'profile_ids':profile,
        'text': text}
    requests.post(url, data = data)
