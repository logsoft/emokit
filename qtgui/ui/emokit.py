# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PySide import QtGui, QtCore
from Ui_emokit import Ui_MainWindow
from Ui_sensor import Ui_uisensor
import pyqtgraph as pg

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.sensors = 'AF3 F7 F3 FC5 T7 P7 O1 O2 P8 T8 FC6 F4 F8 AF4'.split(' ')
        self.senswidgets = {}
        self.add_button = QtGui.QPushButton("Add Items ")
        # self.senswidgets = {}
        # for i, sens in enumerate(self.sensors):
        #     # self.senswidgets[sens] = QtGui.QPushButton("Add Items %s" %sens)
        #     dial_gain = QtGui.QDial(self)
        #     dial_gain.setNotchesVisible(True)
        #     dial_gain.setObjectName("gain %s" % sens)
        #     self.senswidgets[sens + '_dial'] = dial_gain
        #     self.gl_sens.addWidget(self.senswidgets[sens + '_dial'], i ,0 )
        #     self.senswidgets[sens + '_but'] = QtGui.QPushButton("Add Items %s" %sens)
        #     self.gl_sens.addWidget(self.senswidgets[sens + '_but'], i ,1 )
        # self.gl_sens.setColumnStretch(1,2)
        self.gl_sens.addWidget(pg.PlotWidget(name='test') ,0 ,0)

    @QtCore.Slot("bool")
    def on_action_OpenSetup_triggered(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @QtCore.Slot("bool")
    def on_action_SaveSetup_triggered(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @QtCore.Slot("bool")
    def on_action_OpenConnection_triggered(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @QtCore.Slot("bool")
    def on_action_CloseConnection_triggered(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
