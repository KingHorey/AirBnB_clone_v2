#!/usr/bin/python3

""" Fabric script that distributes an archive to web servers """

from fabric.api import *
from fabric.contrib.console import confirm
import os


env.hosts = ['18.234.253.161', '34.224.4.240']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Distributes archive to web servers """

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        f = archive_path.split('/')[-1].split('.')[0]
        sudo("mkdir -p /data/web_static/releases/{}/".format(f))
        """ directory  archive is to be extracted """
        dirs = "/data/web_static/releases/{}/".format(f)
        sudo("tar -xvf /tmp/{}.tgz -C {}".format(f, dirs))
        sudo("rm /tmp/{}.tgz" .format(f))
        sudo("rm /data/web_static/current")
        new_link = "/data/web_static/current"
        sudo("ln -sf /data/web_static/releases/{} {}".format(f, new_link))
        return True
    except Exception:
        return False
