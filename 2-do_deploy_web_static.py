#!/usr/bin/python3
"""distributes an archive to my web servers"""
import os
from fabric.api import *
from datetime import datetime

# Set the host IP addresses for web-01 && web-02
env.hosts = ['54.237.21.182', '35.175.104.231']
env.user = "ubuntu"


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

def do_deploy(archive_path):
    """use os module to check for valid file path"""
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))
        return True
    return False
