from tkinter import Tk
import app

def main():
    root = Tk()
    root.geometry("505x665+250+50")
    app.App(root)
    root.mainloop()

if __name__ == '__main__':
    main()