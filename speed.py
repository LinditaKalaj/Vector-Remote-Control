import customtkinter as ctk


class Speed(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.move_class = None
        self.vector = None
        self.configure_grid()
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

    def configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def set_move(self, move):
        self.head_slider.bind("<ButtonRelease-1>", self.head_slider_event)
        self.lift_slider.bind("<ButtonRelease-1>", self.lift_slider_event)
        self.wheel_slider.bind("<ButtonRelease-1>", self.wheel_slider_event)
        self.move_class = move

    def head_slider_event(self, value):
        print(value)
        self.move_class.set_head_speed(self.head_slider.get())
        # self.vector.audio.set_master_volume(audio.RobotVolumeLevel.MEDIUM_HIGH)

    def lift_slider_event(self, event):
        lift_speed = int(self.lift_slider.get())
        self.move_class.set_lift_speed(lift_speed)

    def wheel_slider_event(self, event):
        wheel_speed = int(self.wheel_slider.get())
        self.move_class.set_wheel_speed(wheel_speed)