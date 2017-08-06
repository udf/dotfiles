#!/usr/bin/python
# better version of music.sh
# advantages:
#     - python
#     - prints song progress
#     - tells you which player the info is from
#     - continuous output (avoid burning your CPU with unnecessary script restarts)
#     - immediate updates because events
#     - python
#
# disadvantages:
#     - ???

import os
import re
from datetime import timedelta
from socket import socket, AF_UNIX, SOCK_STREAM

import gi
gi.require_version('Playerctl', '1.0')
from gi.repository import Playerctl, GLib

output_width = 112
current_player = None
prev_output = ''

# based on https://github.com/kiike/cmus-remote/blob/master/backend.py
def cmus_get_filename():
    s = socket(AF_UNIX, SOCK_STREAM)
    s.connect(cmus_get_filename.socket_path)

    if s.send(('status\n').encode('ascii')) == 0:
        return 'error getting filename'

    ret = s.recv(4096)
    s.close()

    ret = re.findall(r'file (.+)\n', ret.decode('utf-8'))
    if len(ret) <= 0: return ''

    return os.path.splitext(os.path.basename(ret[0]))[0]
cmus_get_filename.socket_path = os.path.join('/run/', 'user', str(os.getuid()), 'cmus-socket')

def get_status(player):
    status = player.get_property('status')
    return {'': '',
            'Playing': ' ',
            'Paused': ' ',
            'Stopped': ' '}.get(status, f'[{status}]')

def get_position(player, metadata):
    def fmt(tdelta):
        hours, rem = divmod(tdelta.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        if hours > 0:
            return f'{hours:02}:{minutes:02}:{seconds:02}'
        return f'{minutes:02}:{seconds:02}'

    position = fmt(timedelta(microseconds=player.get_property('position')))
    duration = metadata.get('mpris:length', 0)

    if duration > 0:
        return '{}/{}'.format(position, fmt(timedelta(microseconds=duration)))
    return f'{position}'

def get_trackname(player, metadata):
    title = metadata.get('xesam:title', '')
    artist = ', '.join(metadata.get('xesam:artist', ''))

    if artist == '':
        if title == '' and player.get_property('player-name') == 'cmus':
            return cmus_get_filename()
        else:
            return title

    return '{} - {}'.format(artist, title)

def print_status(player=None, metadata=None):
    output = []

    def append_output(data, fmt='{}'):
        if len(data) > 0:
            output.append(fmt.format(data))

    global current_player
    if player is None:
        player = Playerctl.Player()
    current_player = player

    try:
        player.on('play', on_change)
        player.on('pause', on_change)
        player.on('stop', on_change)
        player.on('exit', on_change)
        player.on('metadata', on_change)

        if metadata is None:
            metadata = player.get_property('metadata').unpack()

        append_output(get_status(player))
        append_output(player.get_property('player-name'), '[{}]')

        if player.get_property('status') != "Stopped":
            append_output(get_position(player, metadata), '[{}]')
            append_output(get_trackname(player, metadata), ' {}')

    except GLib.Error as e:
        output = []

    global prev_output
    output = ''.join(output)
    if output != prev_output:
        print(output.ljust(output_width), flush=True)

        prev_output = output
        
    return True

def on_change(player, metadata=None):
    print_status()

GLib.timeout_add(500, print_status)
print_status()
GLib.MainLoop().run()