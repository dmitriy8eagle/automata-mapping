from tkinter import Tk
from tkinter import RIGHT
from tkinter import BOTH
from tkinter import RAISED
from tkinter import Frame
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import Radiobutton
from tkinter import IntVar
from tkinter import StringVar

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import formula
import calcs

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.parent.resizable(False, False)
        self.initUI()
        
    def initUI(self):
        self.parent.title("Mapping Charts")
        
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        self.initParentWindow()
        self.initFrameUI()

    def initParentWindow(self):
        calcButton = Button(self, text = "Calculate", command=self.callCalculateFormula)
        calcButton.pack(side = RIGHT, padx = 5, pady = 5, ipadx = 10)

    def initFrameUI(self):
        self.formulaDialogOn = False
        self.reactiveFormula = StringVar()

        self.mode = IntVar()
        Radiobutton(self.frame, text="Sync", variable=self.mode, value=0).grid(row=0, column=0)
        Radiobutton(self.frame, text="Async", state='disabled', variable=self.mode, value=1).grid(row=0, column=1)
        
        formulaLabel = Label(self.frame, text = "F(x) =")
        formulaLabel.grid(row = 1, column = 0, padx = 5, pady = 5)
        formulaValue = Entry(self.frame, textvariable = self.reactiveFormula, state='disabled', width=50)
        formulaValue.grid(row = 1, column = 1, columnspan = 5, pady = 5)
        formulaValue.bind("<Button-1>", self.openFormulaDialog)

        k_label = Label(self.frame, text = "k =")
        k_label.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.k_value = Entry(self.frame, width=50)
        self.k_value.grid(row = 2, column = 1,  columnspan = 5, pady = 5)

        self.initPlot()

    def initPlot(self):
        x = [0]
        y = [0]
        figure = Figure(figsize=(5,5), dpi=100)
        subplot = figure.add_subplot(111)
        self.dataset, = subplot.plot(x, y, ',')
        subplot.set_xlim([0, 1])
        subplot.set_ylim([0, 1])
        self.canvas = FigureCanvasTkAgg(figure, master=self.frame)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row = 3, column = 0, columnspan = 5)

    def openFormulaDialog(self, event):
        if (self.formulaDialogOn):
            return

        self.formulaDialogOn = True
        inputDialog = formula.Dialog(self.parent, self.reactiveFormula.get())
        self.parent.wait_window(inputDialog.top)
        self.formulaDialogOn = False
        self.reactiveFormula.set(inputDialog.formula)
        
    def callCalculateFormula(self):
        k = self.k_value.get()
        try:
            k = int(k)
        except ValueError:
            return
        formula = self.reactiveFormula.get()
        if (formula == '' or k <= 0):
            return
        new_values = calcs.execute_formula(self.reactiveFormula.get(), k)

        self.dataset.set_xdata(new_values['x'])
        self.dataset.set_ydata(new_values['y'])
        self.canvas.draw()