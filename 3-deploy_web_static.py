#!/usr/bin/python3
""" module that creates and distributes an archive to your web servers,
 using the function deploy
 """

from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

@task
def deploy():
    """ that creates and distributes an archive to your web servers """
    path = do_pack()
    if path:
        return do_deploy(path)
    else:
        return False
