#!/bin/sh
# usage: screenshot [-s] [-o filename] [-e /path/to/image_editor]
set -e

args=""
editor=""
filename=$(date +"$HOME/screenshots/screenshot_%Y-%m-%d_%H.%M.%S.png")
while getopts ":o:e:s" flags; do
  case $flags in
    s) args="-s -b 1" ;;
    o) filename=${OPTARG} ;;
	e) editor=${OPTARG} ;;
  esac
done

maim $filename $args -q
[[ ! -z $editor ]] && $editor "$filename"
xclip -se c -t image/png "$filename"
