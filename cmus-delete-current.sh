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

mv "$filepath" "/run/media/dank/Booty/Music/_trash/"  || {
	echo "yo i couldn't move the file"
	exit 3
}

cmus-remote -n