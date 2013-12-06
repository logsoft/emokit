# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emokit.ui'
#
# Created: Fri Dec  6 09:32:47 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 776)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gl_top = QtGui.QGridLayout()
        self.gl_top.setObjectName("gl_top")
        self.comboBox_connection = QtGui.QComboBox(self.centralwidget)
        self.comboBox_connection.setObjectName("comboBox_connection")
        self.gl_top.addWidget(self.comboBox_connection, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(938, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gl_top.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gl_top, 0, 0, 1, 1)
        self.gl_sens = QtGui.QGridLayout()
        self.gl_sens.setObjectName("gl_sens")
        self.gridLayout_3.addLayout(self.gl_sens, 1, 0, 1, 1)
        self.gridLayout_3.setRowStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1076, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_OpenSetup = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/folder_page.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_OpenSetup.setIcon(icon)
        self.action_OpenSetup.setObjectName("action_OpenSetup")
        self.action_SaveSetup = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_SaveSetup.setIcon(icon1)
        self.action_SaveSetup.setObjectName("action_SaveSetup")
        self.action_OpenConnection = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/page_refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_OpenConnection.setIcon(icon2)
        self.action_OpenConnection.setObjectName("action_OpenConnection")
        self.action_CloseConnection = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_CloseConnection.setIcon(icon3)
        self.action_CloseConnection.setObjectName("action_CloseConnection")
        self.menu_File.addAction(self.action_OpenSetup)
        self.menu_File.addAction(self.action_SaveSetup)
        self.menubar.addAction(self.menu_File.menuAction())
        self.toolBar.addAction(self.action_OpenSetup)
        self.toolBar.addAction(self.action_SaveSetup)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_OpenConnection)
        self.toolBar.addAction(self.action_CloseConnection)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OpenSetup.setText(QtGui.QApplication.translate("MainWindow", "&OpenSetup", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveSetup.setText(QtGui.QApplication.translate("MainWindow", "&SaveSetup", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OpenConnection.setText(QtGui.QApplication.translate("MainWindow", "&OpenConnection", None, QtGui.QApplication.UnicodeUTF8))
        self.action_CloseConnection.setText(QtGui.QApplication.translate("MainWindow", "&CloseConnection", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

