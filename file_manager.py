import sys
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon


class Manager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Manager')
        self.setGeometry(100, 500, 1000, 600)

        self.shown = QFileSystemModel()
        self.shown.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.shown)

        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        self.tree.setWindowTitle('Directory View')
        self.tree.resize(1000, 600)

        windowlayout = QVBoxLayout()
        windowlayout.addWidget(self.tree)
        self.setLayout(windowlayout)

        self.tree.doubleClicked(self.type)

    def type(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Manager()
    ex.show()
    sys.exit(app.exec_())
