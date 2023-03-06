import customtkinter as ctk


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configure_style()

    def configure_style(self):
        self.configure(background='#303030')
        self.title("ezVector Setup")
        ctk.set_default_color_theme("green")

        # Set min and max sizes
        width = 500
        height = 700
        self.minsize(400, 600)
        self.maxsize(500, 700)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        # Centers window based on users monitor
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))