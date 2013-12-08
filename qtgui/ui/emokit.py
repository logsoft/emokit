# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import collections
from PySide import QtGui, QtCore
from Ui_emokit import Ui_MainWindow
from Ui_sensor import Ui_uisensor
import pyqtgraph as pg
# from ui.gethread import geThread
from ui.qtemotiv import Emotiv
from ui.qtemotiv import sensorBits
import numpy as np

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
        self.emotiv = Emotiv()
        self.serial, device = self.emotiv.setupposix()
        self.emotiv.opencon('/dev/hidraw4', self.serial)
        self.emotiv.packet.connect(self.update)

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
        # Data stuff
        self.sampleinterval=0.1
        self.timewindow=1000.
        self._interval = int(self.sampleinterval*1000)
        self._bufsize = int(self.timewindow/self.sampleinterval)
        self.databuffer = collections.deque([0.0]*self._bufsize, self._bufsize)
        self.databuffer2 = collections.deque([0.0]*self._bufsize, self._bufsize)
        self.x = np.linspace(-self.timewindow, 0.0, self._bufsize)
        self.y = np.zeros(self._bufsize, dtype=np.float)
        self.y2 = np.zeros(self._bufsize, dtype=np.float)
        # PyQtGraph stuff
        self.plt = pg.PlotWidget(name='test')
        self.plt.showGrid(x=True,y=True)
        self.plt.setLabel('left', 'amplitude', 'V')
        self.plt.setLabel('bottom', 'time', 's')
        self.curve = self.plt.plot(self.x, self.y, pen=(255,0,0))
        self.curve2 = self.plt.plot(self.x, self.y, pen=(255,255,0))
        self.gl_sens.addWidget(self.plt, 0 ,0)

    def __del__(self):
        self.emotiv.closecon()

    def closeEvent(self, event):
        self.emotiv.closecon()

    def genplot(self):
        pass



    def update(self,packet):
        value = packet['F4']['value']

        self.databuffer.append( value)
        self.y[:] = self.databuffer

        value = packet['F7']['value']
        self.databuffer2.append( value)
        self.y2[:] = self.databuffer2
        self.curve.setData(self.y)
        self.curve2.setData(self.y2)

        self.progressBar.setValue(packet['Battery']['value'])



    @QtCore.Slot()
    def on_pBconnect_released(self):
        """
        Slot documentation goes here.
        """
        dev = self.lEdev.text()
        self.emotiv.opencon(dev, self.serial)

    @QtCore.Slot()
    def on_pBdisconnect_released(self):
        """
        Slot documentation goes here.
        """
        self.emotiv.closecon()


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
