#!/usr/bin/python3
""" compressing files before seding module"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """create a .tgz archive from web_static folder"""
    # get the cureent time and date
    time = datetime.now().strftime("%Y%m%d%H%M%S")

    # create a directory
    local("mkdir -p versions")

    # path where the archive file will be stored
    path = "versions/web_static_{}.tgz".format(time)

    # create a compressed file
    archived = local("tar -cvzf {} web_static".format(path))

    # Check archive Creation Status
    if archived.return_code != 0:
        return None
    else:
        return path
