import os

import cons


def is_project_recognized():
    # assume project with python backend and js frontend
    return (
        os.path.isdir('backend')
        and os.path.isdir('frontend')
    )


def execute_script(fname):
    print(f'INFO: Executing {fname}')
    fpath = os.path.join(cons.SCRIPTS_DIR, fname)
    if os.system(fpath):
        print(f'ERROR: executing {fname}')
        exit(1)
    print(f'INFO: Finished {fname}')


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
