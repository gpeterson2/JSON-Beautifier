import sys

from PySide2.QtWidgets import QApplication

from json_beautifier.beautifier.gui import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()


if __name__ == '__main__':
    main()
