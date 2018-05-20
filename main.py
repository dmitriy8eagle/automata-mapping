from tkinter import Tk
import app

def main():
    root = Tk()
    root.geometry("505x635+250+50")
    run = app.App(root)
    root.mainloop()

if __name__ == '__main__':
    main()