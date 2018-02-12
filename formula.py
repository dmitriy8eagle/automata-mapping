from tkinter import Tk, Toplevel, StringVar, Label, Entry, Button

large_font = ('Verdana', 16)

class Dialog:
    def __init__(self, parent, val):
        top = self.top = Toplevel(parent)
        self.formula = ''
        self.reactiveFormula = StringVar(value=val)
        self.label = Label(top, text='Enter your formula below')
        self.label.grid(row=0, columnspan=8)
        self.entryBox = Entry(top, width=30, textvariable = self.reactiveFormula, font=large_font)
        self.entryBox.grid(row=1, columnspan=8, pady=3)
        Button0 = Button(top, width=15, text="1", command = lambda:self.btnPress('1'))
        Button0.grid(row = 2, column = 0)
        Button1 = Button(top, width=15, text="2", command = lambda:self.btnPress('2'))
        Button1.grid(row = 2, column = 1)
        Button2 = Button(top, width=15, text="3", command = lambda:self.btnPress('3'))
        Button2.grid(row = 2, column = 2)
        Button2 = Button(top, width=15, text="4", command = lambda:self.btnPress('4'))
        Button2.grid(row = 2, column = 3)
        Button2 = Button(top, width=15, text="5", command = lambda:self.btnPress('5'))
        Button2.grid(row = 3, column = 0)
        Button2 = Button(top, width=15, text="6", command = lambda:self.btnPress('6'))
        Button2.grid(row = 3, column = 1)
        Button2 = Button(top, width=15, text="7", command = lambda:self.btnPress('7'))
        Button2.grid(row = 3, column = 2)
        Button2 = Button(top, width=15, text="8", command = lambda:self.btnPress('8'))
        Button2.grid(row = 3, column = 3)

        self.mySubmitButton = Button(top, width=30, text='Submit', command=self.send)
        self.mySubmitButton.grid(row = 4, columnspan=8, pady=10)

    def btnPress(self, val):
        self.formula = self.reactiveFormula.get() + str(val)
        self.reactiveFormula.set(self.formula)
        self.entryBox.icursor(len(self.formula))

    def send(self):
        self.formula = self.entryBox.get()
        self.top.destroy()