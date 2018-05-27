from tkinter import Tk
import app

def main():
    root = Tk()

    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    positionRight = int(root.winfo_screenwidth()/2.5 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/3.5 - windowHeight/2)

    root.geometry("+{}+{}".format(positionRight, positionDown))

    app.App(root)
    root.mainloop()

if __name__ == '__main__':
    main()