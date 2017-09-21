#!/bin/bash

cmus-remote -Q &> /dev/null || {
    echo "yo cmus ain't running or something"
    exit 1
}

filepath="$(cmus-remote -Q | awk '/file/ {print $0}' | cut -d ' ' -f 2-)"

if [[ -z "$filepath" ]]; then
    echo "i couldn't get find any playing file"
    exit 2
fi

destination="$1"
if [[ $filepath == *pending_yt* ]]; then
    if [[ $destination == trash ]]; then
        rm "$filepath"
        exit 0
    else
        destination="$HOME/Music/pending_wub"
    fi
else
    if [[ $destination == trash ]]; then
        destination="$HOME/Music/_trash"
    else
        destination="$HOME/Music/_favourites"
    fi
fi

mv "$filepath" "$destination"  || {
   echo "yo i couldn't move the file"
   exit 3
}