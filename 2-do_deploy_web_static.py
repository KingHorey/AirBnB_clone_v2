#!/usr/bin/python3

from fabric.api import local, run, sudo, put, env


def do_deploy(archive_path):
    """ Distributes archive to web servers """
    checks = local(" [ -f {} ]" .format(archive_path))
    if checks.failed:
        return False
    env.hosts = ['18.234.253.161', '34.224.4.240']
    env.users = ["ubuntu"]
    try:
        put(archive_path, '/tmp/')
        f = archive_path.split('/')[-1].split('.')[0]
        sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(f, f))
        sudo("rm /tmp/{}" .format(fil))
        sudo("rm /data/web_static/current")
        new_link = "/data/web_static/current"
        sudo("ln -sf /data/web_static/releases/{} {}".format(f, new_link))
        return True
    except Exception:
        return False
