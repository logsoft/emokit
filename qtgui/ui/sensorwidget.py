# coding=utf-8
__author__ = 'hpl'
from PySide import QtGui, QtCore

class SensorWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SensorWidget, self).__init__(parent)
        self.setMinimumSize(150, 150)
        self.senspos = {
            'AF3' : (30,13,6),
            'F7' : (18,22,6),
            'F3' : (35,25,6),
            'FC5' : (20,38,6),
            'T7' : (8,48,6),
            'P7' : (18,68,6),
            'O1' : (30,81,6),
            'O2' : (65,81,-6),
            'P8' : (77,68,-6),
            'T8' : (87,48,-6),
            'FC6' : (75,38,-8),
            'F4' : (60,25,-6),
            'F8' : (77,22,-6),
            'AF4' : (65,13,-8),
            'REFL' : (12,56,6),
            'REFR' : (83,56,-11),
        }
        self.strenght ={
            'AF3' :0.6,
            'F7' : 0.4,
            'F3' : 0.8,
            'FC5' :1,
            'T7' : 0,
            'P7' : 0,
            'O1' : 0,
            'O2' : 0,
            'P8' : 0,
            'T8' : 0,
            'FC6' :0,
            'F4' : 0,
            'F8' : 0,
            'AF4' :0,
            'REFL' : 0,
            'REFR' : 0,
        }

    def setstrenght(self,sensors):
        for name in sensors:
            try:
                self.strenght[name] = sensors[name]['quality']
            except KeyError:
                pass
        self.repaint()

    def paintEvent(self, event=None):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        side = min(self.width(), self.height())
        painter.setViewport(0,0, side, side)
        painter.setWindow(0, 0, 100, 100)

        self.drawhead(painter)
        self.drawsensor(painter)

        # color = QtGui.QColor()
        # color.setNamedColor('red')
        # painter.setPen(color)
        # for x in range(101):
        #     print x
        #     for y in range(101):
        #         pt = QtCore.QPoint(x,y)
        #         painter.drawPoint(pt)

    def drawsensor(self,qp):
        qp.setPen(QtCore.Qt.black)
        qp.setFont(QtGui.QFont('Helvetica', 3))
        for name in self.senspos:
            x,y,tp = self.senspos[name]
            strenght = self.strenght[name]
            if strenght < 8:
                qp.setBrush(QtCore.Qt.red)
            elif strenght < 13:
                qp.setBrush(QtCore.Qt.yellow)
            else:
                qp.setBrush(QtCore.Qt.green)
            qp.drawEllipse(x, y, 5, 5)
            pt = QtCore.QRect(x+tp,y,x,y)
            qp.drawText(pt, QtCore.Qt.TextSingleLine ,name)

    def drawhead(self, qp):
        color = QtGui.QColor('#FFE2C6')
        qp.setPen(QtCore.Qt.NoPen)
        qp.setBrush(color)
        #head
        qp.drawEllipse(9, 7.5, 82.5, 85)
        #nose
        qp.drawEllipse(42.75, 2.5, 15, 25)
        #left ear
        qp.drawEllipse(4, 40, 15, 20)
        #right ear
        qp.drawEllipse(95, 40, -15, 20)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    form = SensorWidget()
    form.setWindowTitle("Sensor Strenght")
    form.move(0, 0)
    form.show()
    form.resize(400, 400)
    app.exec_()
