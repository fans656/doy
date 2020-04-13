import os
import sys

import util


class Main:

    def __init__(self):
        # TODO: no args supported now
        build()


def build():
    ensure_project_recognized()
    util.ensure_dir('.doy/local')

    build_frontend()
    compress_frontend_dist()
    compress_backend_dist()


def ensure_project_recognized():
    if not util.is_project_recognized():
        print('ERROR: Unrecognized project')
        exit(1)


def build_frontend():
    if not modified():
        print('INFO: Skipping frontend build as source code not changed')
        return
    util.execute_script('build_frontend.sh')


def compress_frontend_dist():
    return util.execute_script('compress_frontend.sh')


def compress_backend_dist():
    return util.execute_script('compress_backend.sh')


def modified():
    # TODO: assume frontend/dist/index.html now
    index_mtime = os.stat('frontend/dist/index.html').st_mtime
    for path, dirs, fnames in os.walk('frontend'):
        if os.path.basename(path) in IGNORED_DIRS:
            dirs[:] = []
        for fname in fnames:
            fpath = os.path.join(path, fname)
            file_mtime = os.stat(fpath).st_mtime
            if file_mtime > index_mtime:
                return True
    return False


IGNORED_DIRS = {
    'node_modules', 'dist',
}
