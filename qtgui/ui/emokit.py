# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import collections
from PySide import QtGui, QtCore
from Ui_emokit import Ui_MainWindow
import pyqtgraph as pg
import osc
from ui.qtemotiv import Emotiv
import numpy as np
from ui.sensorwidget import SensorWidget

color = {
    'F3': (128, 0, 0),
    'FC5': (255, 0, 0),
    'AF3': (0, 128, 0),
    'F7': (0, 255, 0),
    'T7': (0, 0, 128),
    'P7': (0, 0, 255),
    'O1': (128, 128, 0),
    'O2': (255, 128, 0),
    'P8': (255, 255, 0),
    'T8': (128, 255, 0),
    'F8': (255, 0, 128),
    'AF4': (255, 0, 255),
    'FC6': (255, 128, 128),
    'F4': (255, 255, 128),
}


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """


    def __init__(self, parent=None):
        """
        Constructor
        """
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # self.sensors = 'AF3 F7 F3 FC5 T7 P7 O1 O2 P8 T8 FC6 F4 F8 AF4 X Y'.split(' ')
        # self.sensors = 'AF3 F7 F3 FC5 T7 P7 O1 O2 P8 T8 FC6 F4 F8 AF4'.split(' ')
        self.sensors = 'AF3 F7 F3 FC5 P7 O1 O2 P8 FC6 F4 F8 AF4'.split(' ')
        # self.sensors = 'AF3 F7 F3'.split(' ')

        self.updatecnt = 0

        # the emotiv
        self.emotiv = Emotiv()
        self.serial, device = self.emotiv.setupposix()
        if self.serial is not None:
            self.emotiv.opencon('/dev/hidraw4', self.serial)
            self.emotiv.packet.connect(self.update)

        # Data stuff
        self.sampleinterval = 0.1
        self.timewindow = 1000.
        self._bufsize = int(self.timewindow / self.sampleinterval)
        self.x = np.linspace(-self.timewindow, 0.0, self._bufsize)

        #generate data buffer
        self.databuffer = {}
        self.y_axes = {}
        for sens in self.sensors:
            self.databuffer[sens] = collections.deque([0.0] * self._bufsize, self._bufsize)
            # init y axes
            self.y_axes[sens] = np.zeros(self._bufsize, dtype=np.float)

        # PyQtGraph stuff
        self.plt = pg.PlotWidget(name='test')
        self.plt.showGrid(x=True, y=True)
        self.plt.setLabel('left', 'amplitude', 'V')
        self.plt.setLabel('bottom', 'time', 's')

        # generate curves
        self.named_plots = {}
        for sens in self.sensors:
            self.named_plots[sens] = self.plt.plot(self.x, self.y_axes[sens], pen=color[sens])
        self.gl_sens.addWidget(self.plt, 0, 0)

        #sensor quality widget
        self.quality = SensorWidget(self)
        #self.quality.resize(QtCore.QSize(150,150))
        self.gl_quality.addWidget(self.quality, 0, 0)

        #OSC things
        self.oscobj = osc.OscSend()


    def __del__(self):
        self.emotiv.closecon()


    def closeEvent(self, event):
        self.emotiv.closecon()


    def genplot(self):
        pass


    def update(self, packet):
        now = pg.ptime.time()
        for sens in self.sensors:
            value = packet[sens]['value']
            self.databuffer[sens].append(value)

        self.oscobj.sendpacket(packet)

        # value = packet['F7']['value']
        # self.databuffer2.append( value)
        # self.y2[:] = self.databuffer2
        # #self.curve.setData(self.y)
        # self.curve2.setData(self.y2)
        #print "Plot time: %0.2f sec" % (pg.ptime.time()-now)

        if self.emotiv.packetsprocessed > self.updatecnt:
            for sens in self.sensors:
                self.y_axes[sens][:] = self.databuffer[sens]
                self.named_plots[sens].setData(self.y_axes[sens])

            self.updatecnt = self.emotiv.packetsprocessed + 128
            self.statusBar().showMessage("Packets received: %i" % self.emotiv.packetsprocessed)
            self.quality.setstrenght(self.emotiv.sensors)
            if packet['Battery']['value'] > -1:
                self.progressBar.setValue(packet['Battery']['value'])


    @QtCore.Slot('int')
    def on_cBosc_stateChanged(self, p0):
        if p0 == 2:
            self.oscobj.openport(self.lEport.text())
        if p0 == 0:
            self.oscobj.closeport()


    @QtCore.Slot()
    def on_pBconnect_released(self):
        dev = self.lEdev.text()
        self.emotiv.opencon(dev, self.serial)


    @QtCore.Slot()
    def on_pBdisconnect_released(self):
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
        dev = self.lEdev.text()
        self.emotiv.opencon(dev, self.serial)


    @QtCore.Slot("bool")
    def on_action_CloseConnection_triggered(self, checked):
        self.emotiv.closecon()
