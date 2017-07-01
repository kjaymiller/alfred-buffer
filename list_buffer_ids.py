#!/usr/local/bin/python3
"""
This will export the profile_ids to a csv_file.
You can export this CSV into your Alfred List Filter
"""

import requests
import json
import csv

# You will need to register your app to get this token https://buffer.com/developers/apps/create
token = '<YOUR BUFFER TOKEN>'

url = f'https://api.bufferapp.com/1/profiles.json?access_token={token}'
r = requests.get(url)
profiles = json.loads(r.text)
with open('profiles.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for profile in profiles:
        csvwriter.writerow([profile['service_username'], profile['formatted_service'], profile['_id']])
