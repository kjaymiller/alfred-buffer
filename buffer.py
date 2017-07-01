#!/usr/local/bin/python3

import requests
from sys import argv

text = text_formatted = argv[-1]

token = '1/89d5142c6bcb4e961c6b38194ec10832'
url = f'https://api.bufferapp.com/1/updates/create.json?access_token={token}'
profile_ids = [x for x in argv[1:-1]]
for profile in profile_ids:
    data = {'profile_ids':profile,
        'text': text}
    requests.post(url, data = data)
