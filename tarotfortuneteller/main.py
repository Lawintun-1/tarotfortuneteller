import tkinter as tk
from model import Model
from view import View
from controller import Controller

def main():
    root = tk.Tk()
    model = Model()
    view = View(root)
    controller = Controller(model,view)
    view.set_controller(controller)
    view.show_page()
    root.mainloop()

if __name__ == "__main__":
    main()
