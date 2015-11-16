#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication

def get_application_instance():
    instance = QApplication.instance()
    if not instance:
        instance = QApplication(sys.argv)
    return instance

def setPackageDirectory():
    """
    This definition sets the Application package directory in the path.
    """
    packageDirectory = os.path.normpath(os.path.join(os.path.dirname(__file__), "../"))
    packageDirectory not in sys.path and sys.path.append(packageDirectory)
    # print packageDirectory,'----+++'

def setupContributorPaths(thisPath):
    mayaSysPaths = sys.path
    for folder in '/scripts/IECore', '/scripts/IECoreMaya', '/gui','/gui/managers','/gui/foundations','/gui/globals','/gui/resources':
        bufferFolderPath = thisPath + folder

        if bufferFolderPath not in mayaSysPaths:
            try:
                newPath = os.path.normpath(bufferFolderPath)
                sys.path.append("%s" %newPath)
            except:
                print ('%s Failed to append' %bufferFolderPath)