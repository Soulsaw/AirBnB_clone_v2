#!/usr/bin/python3
"""
Write the fabric script ot upload archive to the remote server
"""
from fabric.api import *
from sys import argv
import os
"""Import the local command from the fabric module
"""
# Set the hosts to use the ssh
env.hosts = ['52.91.148.142', '54.87.240.58']
# Set the user to use the ssh
env.user = 'ubuntu'


def do_deploy(archive_path):
    """This function permit to upload a archive file to the server
    """
    if os.path.isfile(archive_path):
        try:
            # Download an archive to the remote server
            name = archive_path.split('/')[-1].split('.')[0]
            put(archive_path, "/tmp/")
            # Create the folder to the unarchive path
            unarchive_path = f"/data/web_static/releases/{name}/"
            run(f"mkdir -p {unarchive_path}")
            # Unarchive the .tgz file to the given path
            run(f"tar -xzf /tmp/{name}.tgz -C {unarchive_path}")
            # Remove the archive file from the server
            run(f"rm /tmp/{name}.tgz")
            # Move the content of the folder web_static inside the
            # unarchive path to an unarchive path
            run(f"mv {unarchive_path}/web_static/* {unarchive_path}")
            # Delete the web_static folder inside the unarchive folder
            run(f"rm -rf {unarchive_path}/web_static")
            # Revome the old symbolic link and create a new
            symlink = f"/data/web_static/current"
            run(f"rm -rf {symlink}")
            run(f"ln -s {unarchive_path} {symlink}")
            return True
        except Exception as e:
            return False
    else:
        return False
