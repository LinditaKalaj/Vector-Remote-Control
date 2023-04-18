import gui
from menu import MenuBar

if __name__ == "__main__":
    # Adds menu bar to Vectors control window and displays window
    root = gui.Window()
    menubar = MenuBar(root)
    menubar.grid(row=0, column=0, columnspan=5, sticky="new")
    root.mainloop()
