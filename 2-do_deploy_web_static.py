#!/usr/bin/python3
from fabric.api import local, put, env, run
from datetime import datetime
from os import path, stat

env.hosts = ['35.190.149.202', '104.196.47.38']
env.user = 'ubuntu'


def do_deploy(archive_path):

    if not archive_path:
        return(False)
    name = archive_path.split('/')[1]

    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(name, name))
        run("rm /tmp/{}".format(name))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        print("New version deployed")
        return(True)

    except Exception as e:
        return(False)
