#!/usr/bin/python3
from fabric.api import local, put, env, run
from datetime import datetime
from os import path, stat

env.hosts = ['35.190.149.202', '104.196.47.38']
env.user = 'ubuntu'


def do_pack():
    var = datetime.now()
    f = "web_static_{}{}{}{}{}{}.tgz".format(var.year, var.month, var.day,
                                           var.hour, var.minute, var.second)
    local("mkdir -p versions")
    local("tar -cvzf versions/{} web_static".format(f))
    print("web_static packed: versions/{} -> {}"
          .format(f, stat('versions/' + f).st_size))

    return "versions/{}".format(filename)

def do_deploy(archive_path):

    if not path.isfile(archive_path):
        return False

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

def deploy():
    try:
        archive_path = do_pack()
        return do_deploy(archive_path)
    
    except BaseException:
        return False
