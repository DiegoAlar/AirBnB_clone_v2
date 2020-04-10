#!/usr/bin/python3
""" deletes out-of-date archives, using the function do_clean """


from fabric.api import *


env.hosts = ['35.237.89.95', '3.80.128.164']


def do_clean(number=0):
    """ function to clean local and servers """
    path_local = 'versions'
    path_servers = "/data/web_static/releases"
    num = eval(number)
    if number == 0 or number == 1:
        # new_number = 1
        number = 1
    # else:
    #     new_number = eval(number) + 1
    with lcd(path_local):
        local("ls -1t | grep -v '/$' | tail -n +{:d} | xargs rm -rf".format(number))
    with cd(path_servers):
        sudo("ls -1t -I test | tail -n +{:d} | xargs rm -rf".format(number))
