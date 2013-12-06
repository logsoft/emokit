# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensor.ui'
#
# Created: Fri Dec  6 07:54:55 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_uisensor(object):
    def setupUi(self, uisensor):
        uisensor.setObjectName("uisensor")
        uisensor.resize(1076, 58)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(uisensor)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dial_gain = QtGui.QDial(uisensor)
        self.dial_gain.setNotchesVisible(True)
        self.dial_gain.setObjectName("dial_gain")
        self.horizontalLayout_2.addWidget(self.dial_gain)
        self.layout_plot = QtGui.QHBoxLayout()
        self.layout_plot.setObjectName("layout_plot")
        self.horizontalLayout_2.addLayout(self.layout_plot)
        self.horizontalLayout_2.setStretch(1, 2)

        self.retranslateUi(uisensor)
        QtCore.QMetaObject.connectSlotsByName(uisensor)

    def retranslateUi(self, uisensor):
        uisensor.setWindowTitle(QtGui.QApplication.translate("uisensor", "Form", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    uisensor = QtGui.QWidget()
    ui = Ui_uisensor()
    ui.setupUi(uisensor)
    uisensor.show()
    sys.exit(app.exec_())

