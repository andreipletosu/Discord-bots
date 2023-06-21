import re
import json
import sys
import requests
import urllib.request
import os
import time


INSTAGRAM_USERNAME = os.environ.get('IG_USERNAME')

headers = {
        "Host": "www.instagram.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
html = requests.get("https://www.instagram.com/" +
                        INSTAGRAM_USERNAME + "/feed/?__a=1", headers=headers)


test = html.json()["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["edge_media_to_caption"]["edges"]

print(test)