#! /usr/bin/evn python

''' The main program. '''

import sys

from PySide import QtGui

from beautifier.window import Window

def main():
    app = QtGui.QApplication(sys.argv)

    widget = Window()
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

