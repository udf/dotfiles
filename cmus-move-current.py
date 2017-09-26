#!/usr/bin/python3

import os
import re
from socket import socket, AF_UNIX, SOCK_STREAM
import sys
import configparser


# Based on https://github.com/kiike/cmus-remote/blob/master/backend.py
def cmus_get_filepath():
    s = socket(AF_UNIX, SOCK_STREAM)
    try:
        s.connect(cmus_get_filepath.socket_path)
    except:
        raise RuntimeError('cmus Is not running.')

    if not s.send(b'status\n'):
        raise RuntimeError('Failed to send status command.')

    recv = s.recv(4096)
    s.close()

    result = re.findall(r'file (.+)', recv.decode('utf-8'))
    if not result:
        raise RuntimeError('Failed get file path.')
        
    return result[0]

cmus_get_filepath.socket_path = os.path.join(
    '/run', 'user', str(os.getuid()), 'cmus-socket'
)

#td:replace with notification
def output(prefix, message):
    if not message: return
    return print('{}: {}'.format(prefix, message))


try:
    dest_key = ' '.join(sys.argv[1:])
    if not dest_key:
        raise RuntimeError('No destination provided.')

    filepath = cmus_get_filepath()
    if not os.path.isfile(filepath):
        raise RuntimeError(f'Could not find "{filepath}".')

    path, filename = os.path.split(filepath)
    os.chdir(path)
    if not os.path.isfile('move_target.ini'):
        raise RuntimeError

    config = configparser.ConfigParser()
    config.read('move_target.ini')
    if dest_key not in config.sections() or 'path' not in config[dest_key]:
        raise RuntimeError

    dest = config[dest_key]['path']

    if dest == '/dev/null':
        output('Deleted', f'{filename}')
        os.remove(filename)
    else:
        output('Moved', f'{filename} to {dest}')
        os.rename(filepath, os.path.join(dest, filename))
except RuntimeError as e:
    output('Error', str(e))
    exit(1)
except Exception as e:
    output('Oh no, something bad happened')
    raise e
