# alfred-buffer

## WARNING:
**As of October 14, 2019 - Buffer has closed access to their API** This workflow will not be maintained until announcement of a new API.**

This Alfred Workflow allows you to rapidly post to your buffer profiles.
![](http://i.imgur.com/u5HDCTv.gif)

## Requirements
* Python 3.6 (I use f-strings *because they are awesome!*)
* [Requests](http://docs.python-requests.org/en/master/) (Makes the API calls easier)
* A buffer single-user token (create one at https://buffer.com/developers/apps/create)
* [Alfred Powerpack](https://www.alfredapp.com/powerpack/)

## Steps
* Replace `<YOUR BUFFER TOKEN>` with your buffer token
* run `list_buffer_ids.py` to generate your csv file
* Select `Buffer Post.alfredworkflow`
* add your csv to the to the list filter
![](http://i.imgur.com/ZdCbBqi.gif)
