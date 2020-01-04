#!/usr/bin/env bash
#Script that generates a .tgz archive from the contents of the web_static folder of the AirBnB Clone repo

import os
from datetime import datetime
from fabric.operations import (local, run)


def do_pack():

    tm = datetime.now()
    date = tm.strftime("%Y%m%d%H%M%S")

    try:
    
        if not os.path.isdir("versions"):
            local("mkdir versions")
 
        files = local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return files

    except:
        return None
