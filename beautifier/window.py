#! /usr/bin/evn python

from PySide import QtCore, QtGui

from .beautifier import beautify

class Window(QtGui.QWidget):
    ''' The main window for the program. '''

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        vbox = QtGui.QVBoxLayout(self)

        # Main text area
        self.textEdit = QtGui.QPlainTextEdit()

        beautify_button = QtGui.QPushButton('Beautify')

        # Options
        self.sort_keys_check = QtGui.QCheckBox('Sort Keys')
        self.indent = QtGui.QLineEdit('4')
        self.indent.setMaxLength(4)
        self.indent.setInputMask('9')

        # Set up the layout.
        hbox = QtGui.QHBoxLayout(self)
        hbox.addWidget(self.sort_keys_check)
        hbox.addWidget(QtGui.QLabel('Indent'))
        hbox.addWidget(self.indent)

        # Add all of the widget to the main layout.
        vbox.addWidget(self.textEdit)
        vbox.addLayout(hbox)
        vbox.addWidget(beautify_button)

        self.setLayout(vbox)

        self.setWindowTitle('JSON Beautifier')

        self.connect(beautify_button,
            QtCore.SIGNAL('clicked()'), self.beautify_json)

    def beautify_json(self):
        ''' Runs when the button is hit. '''

        json_string = unicode(self.textEdit.toPlainText())
        indent = unicode(self.indent.text())
        sort_keys = self.sort_keys_check.isChecked()

        try:
            indent = int(indent)
        except:
            indent = '4'

        # in case something happens, leave the original text
        cleaned = json_string
        if len(json_string) > 0:
            try:
                cleaned = beautify(json_string,
                    sort_keys=sort_keys,
                    indent=indent)
            except Exception as e:
                QtGui.QMessageBox.information(self, u'Error', unicode(e))

        self.textEdit.setPlainText(cleaned)

