class Utils:
    """
    Class used to format window and grid

    Attributes
    ----------

    self.window: object
        Pointer to the current window to be configured

    Methods
    -------
    configure_style(self, title, width, height)
        window configuration
    configure_grid(self, row, col)
        adds the amount of rows and columns specified to the grid
    """
    def __init__(self, window):
        self.window = window

    def configure_style(self, title, width, height):
        """Changes title of window and size of window. Centers the window as well and gives it a background color

        Parameters
        ----------
        title : str
            the title of the window
        width: int
            the width of the window
        height: int
            the height of the window
        Returns
        -------
        None
        """
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
        """configure the grid to have a certain number of rows and columns

        Parameters
        ----------
        row: int
            the number of rows applied to the grid
        col: int
            the number of columns applied to the grid
        Returns
        -------
        None
        """
        for r in range(row + 1):
            self.window.grid_rowconfigure(r, weight=1)
        for c in range(col + 1):
            self.window.grid_columnconfigure(c, weight=1)
