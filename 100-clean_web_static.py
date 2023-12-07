#!/usr/bin/python3
"""
Write the fabric script that that deletes out-of-date archives
"""
from fabric.api import env, local, run
# Set the hosts to use the ssh
env.hosts = ['52.91.148.142', '54.87.240.58']


def do_clean(number=0):
    """This function delete the out date versions of the archive
    """
    result = local(f"ls -t versions/", capture=True)
    result = result.split()
    for item in result[int(number):]:
        local(f"rm -f versions/{item}")
    remote_results = run(f"ls -t /data/web_static/releases/")
    remote_results = remote_results.split()
    for item in remote_results[int(number):]:
        if item != "test":
            run(f"rm -rf /data/web_static/releases/{item}")
