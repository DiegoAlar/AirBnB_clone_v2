#!/usr/bin/python3
""" Bash script that sets up your web servers for the deployment of
web_static
"""


from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """ script that generates a .tgz archive  """
    local("mkdir -p versions")
    path = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    success = local("tar -cvzf {} web_static".format(path))
    if (success.succeeded):
        size = os.path.getsize("{}".format(path))
        print("web_static packed: {} -> {}Bytes".format(path, size))
        return path
    return None
