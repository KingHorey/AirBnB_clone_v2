#!/usr/bin/python3

from fabric.api import local
""" import local function to run on local machine """
from datetime import datetime


def do_pack():
    """ Function generates .tgz archive """
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    hour = datetime.now().hour
    minute = datetime.now().minute
    seconds = datetime.now().second
    local("mkdir versions")
    time_stamp = "{}{}{}{}{}{}".format(year, month, day, hour, minute, seconds)
    cmd = local("tar -cvzf ./versions/web_static_{}.tgz ./web_static"
                .format(time_stamp), capture=True)
    if cmd.failed:
        return None
    else:
        return cmd
