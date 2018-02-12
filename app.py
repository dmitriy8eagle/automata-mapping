from tkinter import Tk, RIGHT, BOTH, RAISED, Frame, Button, Label, Entry, Radiobutton, IntVar, StringVar
import formula

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title("Mapping Charts")
        
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        self.initParentWindow()
        self.initFrameUI()

    def initParentWindow(self):
        calcButton = Button(self, text = "Calculate")
        calcButton.pack(side = RIGHT, padx = 5, pady = 5, ipadx = 10)

    def initFrameUI(self):
        self.formulaDialogOn = False
        self.reactiveFormula = StringVar()

        self.mode = IntVar()
        Radiobutton(self.frame, text="By Formula", variable=self.mode, value=0).grid(row=0, column=0)
        Radiobutton(self.frame, text="Automata", state='disabled', variable=self.mode, value=1).grid(row=0, column=1)
        
        formulaLabel = Label(self.frame, text = "F(x) =")
        formulaLabel.grid(row = 1, column = 0, padx = 5, pady = 5)
        formulaValue = Entry(self.frame, textvariable = self.reactiveFormula, state='disabled', width=60)
        formulaValue.grid(row = 1, column = 1, padx = 1, pady = 5)
        formulaValue.bind("<Button-1>", self.openFormulaDialog)

    def openFormulaDialog(self, event):
        if (self.formulaDialogOn):
            return
        self.formulaDialogOn = True
        inputDialog = formula.Dialog(self.parent, self.reactiveFormula.get())
        self.parent.wait_window(inputDialog.top)
        self.formulaDialogOn = False
        self.reactiveFormula.set(inputDialog.formula)
        print('Formula: ', inputDialog.formula)