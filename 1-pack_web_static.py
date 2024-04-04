#!/usr/bin/python3
"""
genereate tgz archive from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    archiving the web_static folder
    """

    t = datetime.now()
    arch = 'web_static_' + t.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    archive = local('tar -cvzf versions/{} web_static'.format(arch))
    if archive is None:
        return None
    return arch
