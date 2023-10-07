#!/usr/bin/python3
"""
Distributing an archive to your web servers module
"""
from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime

env.hosts = ['54.237.21.182', '35.175.104.231']
env.user = 'ubuntu'


def do_pack():
    """create a .tgz archive from web_static folder"""
    # get the current time and date
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
    """Distribute an archive to your web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Extract the archive to the folder /data/web_static/releases/<archive filename without extension>
        archive_filename = archive_path.split("/")[-1]
        archive_folder = archive_filename.replace(".tgz", "")
        remote_path = "/data/web_static/releases/{}".format(archive_folder)
        run("mkdir -p {}".format(remote_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, remote_path))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current on the web server
        run("ln -s {} /data/web_static/current".format(remote_path))

        print("New version deployed!")
        return True
    except Exception as e:
        return False
