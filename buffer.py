#!/usr/local/bin/python3
"""
Capture your text in quotes and make it the final argument
Add the profile IDs of your choice (separate with a space)

TODOS:
 * Find a way to select multiple accounts at once so this isn't necessary. Support with buffer required.
 * Select the first account as the default and let people know
"""

import requests
from sys import argv

# You will need to register your app to get this token https://buffer.com/developers/apps/create
token = '<YOUR BUFFER TOKEN>'

text = text_formatted = argv[-1]
url = f'https://api.bufferapp.com/1/updates/create.json?access_token={token}'
profile_ids = [x for x in argv[1:-1]]
for profile in profile_ids:
    data = {'profile_ids':profile,
        'text': text}
    requests.post(url, data = data)
