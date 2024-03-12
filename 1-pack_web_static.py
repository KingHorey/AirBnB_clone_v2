#!/usr/bin/python3

from fabric.api import local
""" import local function to run on local machine """
from datetime import datetime


def do_pack():
    """ Function generates .tgz archive """
    dates = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    local("mkdir versions")
    file_name = "versions/web_static_{}.tgz".format(dates)
    cmd = local("tar -cvzf versions/web_static_{}.tgz ./web_static"
                .format(file_name))
    if cmd.failed:
        return None
    else:
        return file_name
