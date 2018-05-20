from tkinter import Tk
from tkinter import Toplevel
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import Button

large_font = ('Verdana', 16)

class Dialog:
    def __init__(self, parent, val):
        top = self.top = Toplevel(parent)
        top.resizable(False, False)
        top.geometry("400x160+270+180")
        self.formula = ''
        self.reactiveFormula = StringVar(value=val)
        self.label = Label(top, text='Enter your formula below')
        self.label.grid(row=0, columnspan=8)
        self.entryBox = Entry(top, width=30, textvariable = self.reactiveFormula, font=large_font)
        self.entryBox.grid(row=1, columnspan=8, pady=3)
        Button0 = Button(top, width=20, text="pow(a, b)", command = lambda:self.btnPress('pow(a,b)'))
        Button0.grid(row = 2, column = 0)
        Button1 = Button(top, width=20, text="sqrt(a)", command = lambda:self.btnPress('sqrt(a)'))
        Button1.grid(row = 2, column = 1)
        Button2 = Button(top, width=20, text="OR", command = lambda:self.btnPress('OR'))
        Button2.grid(row = 2, column = 2)
        Button3 = Button(top, width=20, text="AND", command = lambda:self.btnPress('AND'))
        Button3.grid(row = 3, column = 0)
        Button4 = Button(top, width=20, text="XOR", command = lambda:self.btnPress('XOR'))
        Button4.grid(row = 3, column = 1)
        Button8 = Button(top, width=20, text="+", command = lambda:self.btnPress('+'))
        Button8.grid(row = 3, column = 2)
        Button9 = Button(top, width=20, text="-", command = lambda:self.btnPress('-'))
        Button9.grid(row = 4, column = 0)
        Button10 = Button(top, width=20, text="*", command = lambda:self.btnPress('*'))
        Button10.grid(row = 4, column = 1)
        Button11 = Button(top, width=20, text="/", command = lambda:self.btnPress('/'))
        Button11.grid(row = 4, column = 2)

        self.mySubmitButton = Button(top, width=30, text='Submit', command=self.send)
        self.mySubmitButton.grid(row = 5, columnspan=8, pady=10)

    def btnPress(self, val):
        self.formula = self.reactiveFormula.get() + str(val)
        self.reactiveFormula.set(self.formula)
        self.entryBox.icursor(len(self.formula))

    def send(self):
        self.formula = self.entryBox.get()
        self.top.destroy()