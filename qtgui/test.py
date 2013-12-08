# __author__ = 'hpl'
# import PySide
#
#
#
# from pyqtgraph.Qt import QtGui, QtCore
# import numpy as np
# import pyqtgraph as pg
#
# #QtGui.QApplication.setGraphicsSystem('raster')
# app = QtGui.QApplication([])
# mw = QtGui.QMainWindow()
# mw.setWindowTitle('pyqtgraph example: PlotWidget')
# mw.resize(800,800)
# cw = QtGui.QWidget()
# mw.setCentralWidget(cw)
# l = QtGui.QVBoxLayout()
# cw.setLayout(l)
#
# pw = pg.PlotWidget(name='Plot1')  ## giving the plots names allows us to link their axes together
# l.addWidget(pw)
# pw2 = pg.PlotWidget(name='Plot2')
# l.addWidget(pw2)
# pw3 = pg.PlotWidget()
# l.addWidget(pw3)
#
# mw.show()
#
# ## Create an empty plot curve to be filled later, set its pen
# p1 = pw.plot()
# p1.setPen((200,200,100))
#
# ## Add in some extra graphics
# rect = QtGui.QGraphicsRectItem(QtCore.QRectF(0, 0, 1, 5e-11))
# rect.setPen(QtGui.QPen(QtGui.QColor(100, 200, 100)))
# pw.addItem(rect)
#
# pw.setLabel('left', 'Value', units='V')
# pw.setLabel('bottom', 'Time', units='s')
# pw.setXRange(0, 2)
# pw.setYRange(0, 1e-10)
#
# def rand(n):
#     data = np.random.random(n)
#     data[int(n*0.1):int(n*0.13)] += .5
#     data[int(n*0.18)] += 2
#     data[int(n*0.1):int(n*0.13)] *= 5
#     data[int(n*0.18)] *= 20
#     data *= 1e-12
#     return data, np.arange(n, n+len(data)) / float(n)
#
#
# def updateData():
#     yd, xd = rand(10000)
#     p1.setData(y=yd, x=xd)
#
# ## Start a timer to rapidly update the plot in pw
# t = QtCore.QTimer()
# t.timeout.connect(updateData)
# t.start(50)
# #updateData()
#
# ## Multiple parameterized plots--we can autogenerate averages for these.
# for i in range(0, 5):
#     for j in range(0, 3):
#         yd, xd = rand(10000)
#         pw2.plot(y=yd*(j+1), x=xd, params={'iter': i, 'val': j})
#
# ## Test large numbers
# curve = pw3.plot(np.random.normal(size=100)*1e0, clickable=True)
# curve.curve.setClickable(True)
# curve.setPen('w')  ## white pen
# curve.setShadowPen(pg.mkPen((70,70,30), width=6, cosmetic=True))
#
# def clicked():
#     print("curve clicked")
# curve.sigClicked.connect(clicked)
#
# lr = pg.LinearRegionItem([1, 30], bounds=[0,100], movable=True)
# pw3.addItem(lr)
# line = pg.InfiniteLine(angle=90, movable=True)
# pw3.addItem(line)
# line.setBounds([0,200])
#
# ## Start Qt event loop unless running in interactive mode or using pyside.
# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtGui.QApplication.instance().exec_()

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

import collections
import random
import time
import math
import numpy as np

class DynamicPlotter():

    def __init__(self, sampleinterval=0.1, timewindow=10., size=(600,350)):
        # Data stuff
        self._interval = int(sampleinterval*1000)
        self._bufsize = int(timewindow/sampleinterval)
        self.databuffer = collections.deque([0.0]*self._bufsize, self._bufsize)
        self.x = np.linspace(-timewindow, 0.0, self._bufsize)
        self.y = np.zeros(self._bufsize, dtype=np.float)
        # PyQtGraph stuff
        self.app = QtGui.QApplication([])
        self.plt = pg.plot(title='Dynamic Plotting with PyQtGraph')
        self.plt.resize(*size)
        self.plt.showGrid(x=True, y=True)
        self.plt.setLabel('left', 'amplitude', 'V')
        self.plt.setLabel('bottom', 'time', 's')
        self.curve = self.plt.plot(self.x, self.y, pen=(255,0,0))
        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(self._interval)

    def getdata(self):
        frequency = 0.25
        noise = random.normalvariate(0., 1.)
        new = 10.*math.sin(time.time()*frequency*2*math.pi) + noise
        return new

    def updateplot(self):
        self.databuffer.append( self.getdata() )
        self.y[:] = self.databuffer
        self.curve.setData(self.x, self.y)
        #self.app.processEvents()

    def run(self):
        self.app.exec_()

if __name__ == '__main__':

    m = DynamicPlotter(sampleinterval=0.05, timewindow=10.)
    m.run()
