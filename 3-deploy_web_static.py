#!/usr/bin/python3
"""
a python script to deploy web static
"""
import os
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run


env.hosts = ['34.202.234.49', '54.152.235.52']
env.user = "ubuntu"


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers
    Create a tar gzipped archive of the directory web_static.
    """
    # obtain the current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Construct path where archive will be saved
    archive_path = "versions/web_static_{}.tgz".format(now)

    # use fabric function to create directory if it doesn't exist
    local("mkdir -p versions")

    # Use tar command to create a compresses archive
    archived = local("tar -cvzf {} web_static".format(archive_path))

    # Check archive Creation Status
    if archived.return_code != 0:
        return None
    else:
        return archive_path


def do_deploy(archive_path):
    '''use os module to check for valid file path'''
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))
        return True
    return False


def deploy():
    """
    Create and archive and get its path
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
