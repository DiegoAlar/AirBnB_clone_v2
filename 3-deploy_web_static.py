#!/usr/bin/python3
""" module that creates and distributes an archive to your web servers,
 using the function deploy
 """

import os
from fabric.api import *
# from 1-pack_web_static import do_pack
# from 2-do_deploy_web_static import do_deploy
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['35.237.89.95', '3.80.128.164']


def deploy():
    """ that creates and distributes an archive to your web servers """
    path = do_pack()
    if path:
        return do_deploy(path)
    else:
        return False
