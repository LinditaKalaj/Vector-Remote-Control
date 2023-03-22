import customtkinter as ctk
from anki_vector import audio


class Volume(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.vector = None
        self.configure_grid()
        self.volume_label = ctk.CTkLabel(self, text="Volume")
        self.slider = ctk.CTkSlider(self, from_=0, to=4, number_of_steps=4)
        self.volume_label.grid(row=0, column=0, pady=5)
        self.slider.grid(row=1, column=0, pady=(0, 5))
        self.slider.bind("<ButtonRelease-1>", self.slider_event)

    def configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def set_vector(self, robot):
        self.vector = robot

    def slider_event(self, event):
        value = self.slider.get()
        if value == 0.0:
            self.vector.audio.set_master_volume(audio.RobotVolumeLevel.LOW)
        elif value == 1.0:
            self.vector.audio.set_master_volume(audio.RobotVolumeLevel.MEDIUM_LOW)
        elif value == 2.0:
            self.vector.audio.set_master_volume(audio.RobotVolumeLevel.MEDIUM)
        elif value == 3.0:
            self.vector.audio.set_master_volume(audio.RobotVolumeLevel.MEDIUM_HIGH)
        else:
            self.vector.audio.set_master_volume(audio.RobotVolumeLevel.HIGH)
