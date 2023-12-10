#!/usr/bin/python3
"""
Write the fabric script ot create a .tvz archive file
"""
from fabric.api import run
from fabric.api import local
from fabric.api import env
from fabric.api import put
from fabric.api import runs_once
from os.path import isfile, isdir
from datetime import datetime
"""Import the local command from the fabric module
"""
env.hosts = ['52.91.148.142', '54.87.240.58']


def deploy():
    """This function create a archive using the shell
    command line tar -zcvf name.tgz folder
    """
    path = do_pack()
    if isfile(path):
        return do_deploy(path)
    else:
        return False


@runs_once
def do_pack():
    """This function create a archive using the shell command line\
        tar -zcvf name.tgz folder
    """
    if isdir("versions") is False:
        local("mkdir -p versions")
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f"web_static_{timestamp}.tgz"
    result = local(f"tar -zcvf versions/{archive_name} web_static")
    if result.succeeded:
        return f"versions/{archive_name}"
    else:
        return None


def do_deploy(archive_path):
    """This function permit to upload a archive file to the server
    """
    if isfile(archive_path):
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
            print("New version deployed!")
            return True
        except Exception as e:
            return False
    else:
        return False
