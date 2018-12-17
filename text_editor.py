from tkinter import *
from tkinter import filedialog as fd
import tkinter

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


root = tkinter.Tk()
root.title = 'Window'
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text='Open', command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text='Save', command=extract_text)
b2.grid(row=1, column=1, sticky=W)

root.mainloop()
