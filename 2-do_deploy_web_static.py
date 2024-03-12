#!/usr/bin/python3

from fabric.api import local, run, sudo, put, env


def do_deploy(archive_path):
    """ Distributes archive to web servers """
    checks = local(" [ -f {} ]" .format(archive_path))
    if checks.failed:
        return False
    env.hosts = ['18.234.253.161', '34.224.4.240']
    try:
        put(archive_path, '/tmp/')
        fil = archive_path.split('/')[1].split('.')[0]
        sudo("tar -xzf /tmp/{} -C /data/web_static/releases/".format(fil))
        sudo("rm /tmp/{}" .format(fil))
        sudo("rm /data/web_static/current")
        sudo(f"ln -sf /data/web_static/releases/{fil} /data/web_static/current")
        return True
    except Exception:
        return False
