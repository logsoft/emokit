# coding=utf-8
#from PySide.QtGui import QApplication
from PySide import QtGui
import logging
import PySide
import atexit

__author__ = 'hpl'
# -*- coding: utf-8 -*-

import sys
# Import the compiled UI module
from ui.emokit import MainWindow

# Gets a tuple with each version component
pysidever = PySide.__version__
# Prints the Qt version used to compile PySide
qtversion = PySide.QtCore.__version__
#get the python version
pyversion = sys.version.strip('\n')

#setup the logging
logging.basicConfig(handlers=[logging.FileHandler("example1.log"), logging.StreamHandler()],
                    format='%(asctime)s %(name)s: %(levelname)s %(module)s , line %(lineno)d , $ %(message)s',
                    level=logging.DEBUG)
logging.info('pysideversion: %s' % pysidever)
logging.info('compiled to QT version: %s' % qtversion)
logging.info('python version: %s' % pyversion)


def exitthings():
    logging.info('shuting down by user!?')


atexit.register(exitthings)


class PyQtRunner(QtGui.QApplication):
    apps = []

    def __init__(self, args=None, apps=None, exec_=False):
        if args is None:
            args = sys.argv
        super(PyQtRunner, self).__init__(args)

        if apps is not None:
            self.apps.extend(App() for App in apps)
        if exec_:
            self.exec_()

    def add(self, app):
        self.apps.append(app())
        return self

    def exec_(self):
        for a in self.apps:
            a.show()

        sys.exit(super(PyQtRunner, self).exec_())


if __name__ == "__main__":
    PyQtRunner().add(MainWindow).exec_()
