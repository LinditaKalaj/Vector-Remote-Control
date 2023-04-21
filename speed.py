import customtkinter as ctk

from window_utils import Utils


class Speed(ctk.CTkFrame):
    """
    Frame class used to control vectors speed and motors via gui object

    Attributes
    ----------

    self.win_utils: object
        util class to configure the grid
    self.vector: object
        Vector's robot object
    self.move_class: object
        pointer to move class so his motor speeds can be set
    self.head_speed_label: object
        label on the gui for controlling head speed when tilting head
    self.head_slider: object
        slider object that allows the user to pick vectors head speed when tilting head
    self.lift_speed_label: object
        label on the gui for controlling vectors little fork lift arm speed
    self.lift_slider: object
        slider object that allows the user to pick vectors speed for his little fork lift arms
    self.wheel_speed_label: object
        label on the gui for controlling vectors wheel speed
    self.wheel_slider: object
        slider object that allows the user to pick vectors speed wheel motors
    Methods
    -------
    set_move(self, move)
        sets key bindings, so you can move the sliders to set the speed
    head_slider_event(self, value)
        sets head speed in movement class
    lift_slider_event(self, event)
        sets lift speed in movement class
    wheel_slider_event(self, event)
        sets wheel speed in movement class
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.win_utils = Utils(self)
        self.win_utils.configure_grid(5, 0)

        self.vector = None
        self.move_class = None

        self.head_speed_label = ctk.CTkLabel(self, text="Head Speed")
        self.head_slider = ctk.CTkSlider(self, from_=1, to=8, number_of_steps=7)
        self.head_speed_label.grid(row=0, column=0, pady=10)
        self.head_slider.grid(row=1, column=0, pady=(0, 10))

        self.lift_speed_label = ctk.CTkLabel(self, text="Lift Speed")
        self.lift_slider = ctk.CTkSlider(self, from_=1, to=8, number_of_steps=7)
        self.lift_speed_label.grid(row=3, column=0, pady=10)
        self.lift_slider.grid(row=4, column=0, pady=(0, 10))

        self.wheel_speed_label = ctk.CTkLabel(self, text="Wheel Speed")
        self.wheel_slider = ctk.CTkSlider(self, from_=30, to=200, number_of_steps=200)
        self.wheel_speed_label.grid(row=5, column=0, pady=10)
        self.wheel_slider.grid(row=6, column=0, pady=(0, 10))

    def set_move(self, move):
        """ gets movement class pointer,
        sets the bindings and callbacks so the sliders can set the speed in the movement class.

        Parameters
        ----------
        move : object
            pointer to the move class
        Returns
        -------
        None
        """
        self.head_slider.bind("<ButtonRelease-1>", self.head_slider_event)
        self.lift_slider.bind("<ButtonRelease-1>", self.lift_slider_event)
        self.wheel_slider.bind("<ButtonRelease-1>", self.wheel_slider_event)
        self.move_class = move

    def head_slider_event(self, value):
        """ gets the value from the head slider and sets the speed value in the movement class.
        Sets vectors head tilt speed.

        Parameters
        ----------
        value : object
            default var used in callback function but not used. can ignore
        Returns
        -------
        None
        """
        self.move_class.set_head_speed(self.head_slider.get())

    def lift_slider_event(self, event):
        """ gets the value from the lift slider and sets the speed value in the movement class.
        Sets vector's arm speed

        Parameters
        ----------
        event : object
            default var used in callback function but not used. can ignore
        Returns
        -------
        None
        """
        lift_speed = int(self.lift_slider.get())
        self.move_class.set_lift_speed(lift_speed)

    def wheel_slider_event(self, event):
        """ gets the value from the wheel slider and sets the speed value in the movement class.
        Set vector's wheel speed.

        Parameters
        ----------
        event : object
            default var used in callback function but not used. can ignore
        Returns
        -------
        None
        """
        wheel_speed = int(self.wheel_slider.get())
        self.move_class.set_wheel_speed(wheel_speed)
