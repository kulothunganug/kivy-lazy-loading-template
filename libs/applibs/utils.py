import os

from libs.applibs import constants


def abs_path(*path):
    return os.path.join(constants.PROJECT_DIR, *path)
