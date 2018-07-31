#!/usr/bin/python3
from fabric.api import local, put, env
from datetime import datetime
from os import stat

env.hosts = ['localhost']


def do_pack():
    var = datetime.now()
    f = "web_static_{}{}{}{}{}.tgz".format(var.year, var.month, var.day,
                                           var.minute, var.second)
    local("mkdir -p versions")
    local("tar -cvzf versions/{} web_static".format(f))
    print("web_static packed: versions/{} -> {}"
          .format(f, stat('versions/' + f).st_size))

def do_deploy(archive_path):

    if not archive_path:
        return(False)
    name = archive_path.split('/')[1]
    try:
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}".format(name))
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
