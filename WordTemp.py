#-*- coding: utf-8 -*
from docxtpl import DocxTemplate
from tkinter import *
import tkinter as tk
from tkinter import messagebox

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        var_row = 0
        var_column = 0
        self.label = Label(self, text='姓名')
        self.label.grid(row=0, column=0)
        var_column = var_column + 1
        self.xing_ming = Entry(self, width=20)
        self.xing_ming.grid(row=0, column=1)

        var_column = var_column + 1
        self.label2 = Label(self, text='年龄')
        self.label2.grid(row=0, column=2, padx=10)
        self.nian_ling = Entry(self, width=20)
        self.nian_ling.grid(row=0, column=3)

        self.qButton = Button(self, text="生成模板", command=self.generate_template)
        self.qButton.grid(row=2, column=1, columnspan=2)

        self.qButton = Button(self, text="警告", command=self.alert)
        self.qButton.grid(row=3, column=1)


    def alert(self):
        messagebox.showinfo(title='Hi', message='hahahaha')

    def generate_template(self):
        xing_ming = self.xing_ming.get() or 'world'
        nian_ling = self.nian_ling.get() or 'world'

        doc = DocxTemplate("模板.docx")

        context = {
            'xing_ming': xing_ming, 'nian_ling': nian_ling
        }

        doc.render(context)
        doc.save("generated_doc.docx")
        print("end, world")

root = tk.Tk()
root.title("模板生成")
root.geometry("200x100")

app = App(root)
app.place(x=20, y=20)
# app.master.title('Hello')
app.mainloop()

