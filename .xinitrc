#!/bin/bash

numlockx &
xrdb ~/.Xresources
xset -b

dbus-update-activation-environment --systemd DISPLAY
eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
export SSH_AUTH_SOCK
export QT_QPA_PLATFORMTHEME=qt5ct

exec i3
