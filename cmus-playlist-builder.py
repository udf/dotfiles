#!/usr/bin/python

import os
from collections import defaultdict

# build playlists from directories
os.chdir(os.path.expanduser("~/.config/cmus/playlists"))
music_dir = os.path.expanduser("~/Music")
playlists = {
    "_trash" : "trash", 
    "_favourites": "favourites", 
    "pending_yt": "pending_yt", 
    "pending_yt_ka": "pending_yt_ka",
    "pending_wub": "pending_wub",
    "wubwubwub": "wubwubwub"
}

counter = defaultdict(int)

for dir_name, playlist_name in playlists.items():
    dir_path = os.path.join(music_dir, dir_name)
    with open(playlist_name, "w") as outfile:
        for file_name in os.listdir(dir_path):
            print(os.path.join(dir_path, file_name), file=outfile)
            counter[playlist_name] += 1

for playlist,count in counter.items():
    print(f"{count} items in {playlist}")
