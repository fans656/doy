import os
import sys
import json
import subprocess

import util
from build import build


class Main:

    def __init__(self):
        # TODO: no args supported now
        deploy()


def deploy():
    build()
    upload_frontend_dist()


def upload_frontend_dist():
    config = load_config()
    user = config['user']
    host = config['host']
    root = config['root']
    port = config['port']
    name = get_project_name()
    util.execute_script(f'upload_dist.sh {user} {host} {root} {name} {port}')


def get_project_name():
    out = subprocess.check_output('git remote get-url --push origin', shell = True)
    out = out.decode().strip()
    name = out.split('/')[-1]
    if name.endswith('.git'):
        name = name[:-len('.git')]
    return name


def load_config():
    fpath = '.doy/conf.json'
    d = {}
    if os.path.exists(fpath):
        with open(fpath) as f:
            d = json.load(f)
    d['user'] = d['user'] or 'root'
    d['host'] = d['host'] or 'linode'
    d['root'] = d['root'] or '/root'
    d['port'] = d['port'] or 8000
    return d
