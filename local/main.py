#! /usr/bin/env python3
import os
import sys
import argparse
from collections import deque

import util
from deploy import deploy
from build import build


MAIN_USAGE = '''
doy <command> [<args>]

Commands:
    init|i      Initialize a new project
    build|b     Build current project
    deploy|d    Deploy current project
    master      Setup a master node
    slave       Setup a slave node
    help        Help on specific command
'''.strip()


class Main:

    def __init__(self):
        parser = argparse.ArgumentParser(usage = MAIN_USAGE)
        parser.add_argument('command')
        args = parser.parse_args(sys.argv[1:2])
        try:
            cmd = getattr(self, args.command)
        except AttributeError:
            print(f'ERROR: unrecognized command "{args.command}"')
        else:
            sys.argv = sys.argv[2:]
            cmd()

    def init(self):
        raise NotImplementedError()
    i = init

    def build(self):
        build()
    b = build

    def deploy(self):
        deploy()
    d = deploy

    def master(self):
        raise NotImplementedError()

    def slave(self):
        raise NotImplementedError()

    def help(self):
        raise NotImplementedError()


if __name__ == '__main__':
    Main()
