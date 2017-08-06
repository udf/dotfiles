#!/bin/bash
exec 2>/dev/null

icon="$(playerctl status)"
icon="${icon/Playing/ }"
icon="${icon/Paused/ }"
icon="${icon/Stopped/ }"

info="$(playerctl metadata xesam:title)"
artist="$(playerctl metadata xesam:artist)"
if [[ $artist != "" ]]; then
	info="$artist - $info"
fi

printf "%-3s%-109s" "$icon" "$info"