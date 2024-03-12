#!/usr/bin/python3

from fabric.api import local
""" import local function to run on local machine """
from datetime import datetime


def do_pack():
    """ Function generates .tgz archive """
    dates = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    local("mkdir versions")
    cmd = local("tar -cvzf versions/web_static_{}.tgz ./web_static"
                .format(dates))
    if cmd.failed:
        return None
    else:
        return cmd
