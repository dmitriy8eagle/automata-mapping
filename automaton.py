from tkinter import Tk
from tkinter import Toplevel
from tkinter import StringVar
from tkinter import Label
from tkinter import Text
from tkinter import Button
from tkinter import INSERT

large_font = ('Verdana', 16)

class Dialog:
    def __init__(self, parent, val):
        top = self.top = Toplevel(parent)
        top.resizable(False, False)

        windowWidth = top.winfo_reqwidth()
        windowHeight = top.winfo_reqheight()

        positionRight = int(top.winfo_screenwidth()/3.2 - windowWidth/2)
        positionDown = int(top.winfo_screenheight()/2.5 - windowHeight/2)

        top.geometry("+{}+{}".format(positionRight, positionDown))


        self.formula = ''
        self.reactiveAutomaton = StringVar(value=val)
        self.label = Label(top, text='Enter your automaton declaration below')
        self.label.grid(row=0, columnspan=10)
        self.entryBox = Text(top, height=10, width=60, font=large_font)
        self.entryBox.grid(row=1, columnspan=8, pady=3)

        self.mySubmitButton = Button(top, width=30, text='Submit', command=self.send)
        self.mySubmitButton.grid(row = 5, columnspan=8, pady=10)

        self.entryBox.insert(INSERT, self.reactiveAutomaton.get())

    def send(self):
        self.formula = self.entryBox.get("1.0","end-1c")
        self.top.destroy()