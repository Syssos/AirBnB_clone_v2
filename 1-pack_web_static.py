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
