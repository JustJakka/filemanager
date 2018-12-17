import sys
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from tkinter import *
from tkinter import filedialog as fd


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

        window_layout = QVBoxLayout()
        window_layout.addWidget(self.tree)
        self.setLayout(window_layout)

    def text_editor_eval(self):
        def insert_text():
            file_name = fd.askopenfilename()
            with open(file_name) as file:
                txt = file.read()
                text.insert(1.0, txt)

        def extract_text():
            file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                        ("HTML files", "*.html;*.htm"),
                                                        ("All files", "*.*")))
            with open(file_name, mode='w') as file:
                txt = text.get(1.0, END)
                file.write(txt)


        root = Tk()
        text = Text(width=50, height=25)
        text.grid(columnspan=2)
        b1 = Button(text='Open', command=insert_text)
        b1.grid(row=1, sticky=E)
        b2 = Button(text='Save', command=extract_text)
        b2.grid(row=1, column=1, sticky=W)
        root.title = 'Window'

        root.mainloop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Manager()
    ex.show()
    sys.exit(app.exec_())
