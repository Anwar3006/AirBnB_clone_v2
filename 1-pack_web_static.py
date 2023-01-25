#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    time = datetime.now()
    now = time.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))