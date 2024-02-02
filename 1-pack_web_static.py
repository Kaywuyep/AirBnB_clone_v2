#!/usr/bin/python3
"""a fabric script"""
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    # Step 1: Generate a timestamp to be used in the archive filename
    fileName = strftime("%Y%m%d%H%M%S")

    try:
        # Step 2: Create the 'versions' folder if it doesn't exist
        local("mkdir -p versions")

        # Step 3: Compress web_static contents into the archive using tar
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(fileName))

        # Step 4: Return the path of the generated archive if successful
        return "versions/web_static_{}.tgz".format(fileName)

    except Exception as e:
        # Step 5: Return None if any exception occurs during the process
        return None
