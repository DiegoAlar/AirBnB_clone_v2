#!/usr/bin/python3
""" module that creates and distributes an archive to your web servers,
 using the function deploy
 """

from fabric.api import *
# do_pack = __import__('1-pack_web_static').do_pack
# do_deploy = __import__('2-do_deploy_web_static').do_deploy

# def deploy():
#     """ that creates and distributes an archive to your web servers """
#     path = do_pack()
#     if path:
#         return do_deploy(path)
#     else:
#         return False

from datetime import datetime
import os

env.hosts = ['35.237.89.95', '3.80.128.164']

@task
def deploy():
    """ that creates and distributes an archive to your web servers """
    path = do_pack()
    if path:
        return do_deploy(path)
    else:
        return False

@runs_once
def do_pack():
    """ script that generates a .tgz archive  """
    local("mkdir -p versions")
    path = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    print("Packing web_static to {}".format(path))
    success = local("tar -cvzf {} web_static".format(path))
    if (success.succeeded):
        size = os.path.getsize("{}".format(path))
        print("web_static packed: {} -> {}Bytes".format(path, size))
        return path
    return None

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

    