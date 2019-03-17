from PySide2 import QtWidgets

from .beautifier import beautify


class MainWindow(QtWidgets.QWidget):
    ''' The main window for the program. '''

    def __init__(self):
        super(MainWindow, self).__init__()

        vbox = QtWidgets.QVBoxLayout(self)

        # Main text area
        self.textEdit = QtWidgets.QPlainTextEdit()

        beautify_button = QtWidgets.QPushButton('Beautify')

        # Options
        self.sort_keys_check = QtWidgets.QCheckBox('Sort Keys')
        self.indent = QtWidgets.QLineEdit('4')
        self.indent.setMaxLength(4)
        self.indent.setInputMask('9')

        # Set up the layout.
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.sort_keys_check)
        hbox.addWidget(QtWidgets.QLabel('Indent'))
        hbox.addWidget(self.indent)

        # Add all of the widget to the main layout.
        vbox.addWidget(self.textEdit)
        vbox.addLayout(hbox)
        vbox.addWidget(beautify_button)

        self.setLayout(vbox)

        self.setWindowTitle('JSON Beautifier')

        beautify_button.clicked.connect(self.beautify_json)

    def beautify_json(self):
        ''' Runs when the button is hit. '''

        json_string = str(self.textEdit.toPlainText())
        indent = str(self.indent.text())
        sort_keys = self.sort_keys_check.isChecked()

        try:
            indent = int(indent)
        except ValueError as e:
            indent = '4'

        # in case something happens, leave the original text
        cleaned = json_string
        if len(json_string) > 0:
            try:
                cleaned = beautify(json_string, sort_keys=sort_keys,
                                   indent=indent)
            except Exception as e:
                QtWidgets.QMessageBox.information(self, u'Error', str(e))

        self.textEdit.setPlainText(cleaned)
