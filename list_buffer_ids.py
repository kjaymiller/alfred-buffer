#!/usr/local/bin/python3

import requests
import json
import csv

token = '1/89d5142c6bcb4e961c6b38194ec10832'
url = f'https://api.bufferapp.com/1/profiles.json?access_token={token}'
r = requests.get(url)
profiles = json.loads(r.text)
with open('profiles.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for profile in profiles:
        csvwriter.writerow([profile['service_username'], profile['formatted_service'], profile['_id']])
