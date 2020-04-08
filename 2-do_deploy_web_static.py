#!/usr/bin/python3
""" Write a Fabric script (based on the file 1-pack_web_static.py) that
 distributes an archive to your web servers, using the function do_deploy
"""


import os
from fabric.api import *


env.hosts = ['35.237.89.95', '3.80.128.164']


def do_deploy(archive_path):
    """ sends file to server """
    if (os.path.isfile(archive_path)):
        route_tgz = archive_path.split('/')[-1]
        uncomp = archive_path.split('/')[-1].split('.')[0]

        if (put(archive_path, "/tmp/").succeeded and
            sudo("mkdir -p /data/web_static/releases/{}/".
            format(uncomp)).succeeded and
            sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(route_tgz, uncomp)).succeeded and
            sudo("rm /tmp/{}".format(route_tgz)).succeeded and
            sudo("""mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/""".
            format(uncomp, uncomp)).succeeded and
            sudo("rm -rf /data/web_static/releases/{}/web_static".
            format(uncomp)).succeeded and
            sudo("rm -rf /data/web_static/current").succeeded and
            sudo("""ln -s /data/web_static/releases/{}/ \
                /data/web_static/current""".format(uncomp)).succeeded):
            print("New version deployed!")
            return True
    else:
        False
