from tkinter import Menu

import gui
from menu import MenuBar

if __name__ == "__main__":
    root = gui.Window()
    menubar = MenuBar(root)
    menubar.grid(row=0, column=0, columnspan=5, sticky="new")
    root.mainloop()

