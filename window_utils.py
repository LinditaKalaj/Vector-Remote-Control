class Utils:
    def __init__(self, window):
        self.window = window

    def configure_style(self, title, width, height):
        self.window.configure(background='#303030')
        self.window.title(title)

        # Set min and max sizes
        self.window.minsize(width, height)
        self.window.maxsize(width, height)
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        # Centers window based on users monitor
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def configure_grid(self, row, col):
        for r in range(row + 1):
            self.window.grid_rowconfigure(r, weight=1)
        for c in range(col + 1):
            self.window.grid_columnconfigure(c, weight=1)
