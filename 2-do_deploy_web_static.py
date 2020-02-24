##!/usr/bin/python3
"""Script that generates a .tgz archive"""


import os
from datetime import datetime
from fabric.operations import local, run, put, env
env.hosts = ['34.74.218.90', '35.229.122.165']


def do_deploy(archive_path):
    """deploy"""

    if not os.path.exists(archive_path):
        return False
    try:
        base = os.path.basename(archive_path)
        os.path.splitext(base)
        fileEx = os.path.splitext(base)[0]
        file2 = "/data/web_static/releases/"
        file1 = "/tmp/web_static_20200224172428.tgz"
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(fileEx))
        run('tar -xzf {} -C {}{}/'.format(file1, file2, fileEx))
        run('rm {}'.format(file1))
        run('mv {}{}/web_static/* {}{}'.format(file2, fileEx, file2, fileEx))
        run('rm -rf {}{}/web_static'.format(file2, fileEx))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{} /data/web_static/current'.format(file2, fileEx))
        print("New version deployed!")
        return True

    except Exception:
        return False
