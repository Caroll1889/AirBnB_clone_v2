#!/usr/bin/python3
# Script that generates a .tgz archive

import os
from datetime import datetime
from fabric.operations import local, run


def do_pack():

    tm = datetime.now()
    date = tm.strftime("%Y%m%d%H%M%S")

    try:

        if not os.path.isdir("versions"):
            local("mkdir versions")
        file_1 = "versions/web_static_{}.tgz web_static".format(date)
        file_2 = local("tar -cvzf {}".format(file_1))
        return file_2

    except Exception:
        return None
