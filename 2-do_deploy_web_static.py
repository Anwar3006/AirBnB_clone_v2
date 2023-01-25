#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
from datetime import datetime
from fabric.api import *
from os import path


env.hosts = ['100.26.160.22', '100.25.202.194']


def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """
    time = datetime.now()
    now = time.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if path.exists(archive_path):
        archive_file = archive_path.split('/')[1]
        upload_path = f'/tmp/{archive_file}'
        extract_folder = archive_file.split('.')[0]
        extract_path = f'/data/web_static_releases/{extract_folder}/'

        put(archive_path, upload_path)
        run("mkdir -p {}".format(extract_path))
        run("tar -xzf {} -C {}".format(upload_path, extract_path))
        run("rm -rf {}".format(upload_path))
        run("mv -f {}web_static/* {}".format(extract_path, extract_path))
        run("rm -rf {}web_static".format(extract_path))
        run("rm -f /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(extract_path))

        return True
    return False
