from tkinter import Tk
import app

def main():
    root = Tk()
    root.geometry("405x520+250+50")
    run = app.App(root)
    root.mainloop()  

if __name__ == '__main__':
    main()