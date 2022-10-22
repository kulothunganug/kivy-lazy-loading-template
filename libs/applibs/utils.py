import os

from libs.applibs import constants


def abs_path(file):
    return os.path.join(constants.PROJECT_DIR, file)
