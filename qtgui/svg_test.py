__author__ = 'hpl'

sensors = 'AF3 F7 F3 FC5 T7 P7 O1 O2 P8 T8 FC6 F4 F8 AF4'.split(' ')

import sys
from PySide.QtGui import QApplication, QGraphicsScene, QGraphicsView
from PySide.QtWebKit import QGraphicsWebView
import xml.etree.ElementTree as ET

tree = ET.parse('epocheadsimple.svg')
root = tree.getroot()

for child in root.iter('{http://www.w3.org/2000/svg}path'):
    print 'child: ', child
    print 'tag: ', child.tag
    print 'attr: ', child.attrib
    # print child.attrib['id']
    # print child.attrib['fill']



#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     item = QGraphicsWebView()
#     item.load('epochead.svg')
#     view = QGraphicsView()
#     scene = QGraphicsScene()
#     scene.addItem(item)
#     view.setScene(scene)
#     view.show()
#     sys.exit(app.exec_())
