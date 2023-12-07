#!/usr/bin/python3
"""
Write the fabric script ot create a .tvz archive file
"""
from fabric.api import env
from os.path import isfile
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
"""Import the local command from the fabric module
"""
# Set the hosts to use the ssh
env.hosts = ['52.91.148.142', '54.87.240.58']



def deploy():
    """This function create a archive using the shell command line\
        tar -zcvf name.tgz folder
    """
    path = do_pack()
    if isfile(path):
        return do_deploy(path)
    else:
        return False
