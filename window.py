#! /usr/bin/evn python

from PyQt4 import QtCore, QtGui

from beautifier import beautify 

class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        vbox = QtGui.QVBoxLayout(self)

        self.textEdit = QtGui.QPlainTextEdit()
        beautify_button = QtGui.QPushButton('Beautify')

        self.sort_keys_check = QtGui.QCheckBox('Sort Keys')
        self.indent = QtGui.QLineEdit('4')
        self.indent.setMaxLength(4)
        self.indent.setInputMask('9')

        hbox = QtGui.QHBoxLayout(self)
        hbox.addWidget(self.sort_keys_check)
        hbox.addWidget(QtGui.QLabel('Indent'))
        hbox.addWidget(self.indent)

        vbox.addWidget(self.textEdit)
        vbox.addLayout(hbox)
        vbox.addWidget(beautify_button)

        self.setLayout(vbox)

        self.setWindowTitle('JSON Beautifier')

        self.connect(beautify_button, 
            QtCore.SIGNAL('clicked()'), self.beautify_json)

    def beautify_json(self):
        json = unicode(self.textEdit.toPlainText())
        indent = unicode(self.indent.text())
        sort_keys = self.sort_keys_check.isChecked()
        
        try:
            indent = int(indent)
        except:
            indent = '4'
            
        cleaned = json
        if len(json) > 0:
            try:
                cleaned = beautify(json, 
                    sort_keys=sort_keys, 
                    indent=indent)
            except Exception as e:
                QtGui.QMessageBox.information(self, u'Error', unicode(e))

        self.textEdit.setPlainText(cleaned)

