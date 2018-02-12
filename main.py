from tkinter import Tk
import app

def main():
    root = Tk()
    root.geometry("470x420+250+100")
    run = app.App(root)
    root.mainloop()  

if __name__ == '__main__':
    main()