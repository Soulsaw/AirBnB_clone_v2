#!/usr/bin/python3
"""
Write the fabric script ot create a .tvz archive file
"""
from fabric.api import local
from datetime import datetime
"""Import the local command from the fabric module
"""


def do_pack():
    """This function create a archive using the shell command line\
        tar -zcvf name.tgz folder
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f"web_static_{timestamp}.tgz"
    result = local(f"tar -zcvf versions/{archive_name} web_static")
    if result.succeeded:
        return archive_name
    else:
        return None
