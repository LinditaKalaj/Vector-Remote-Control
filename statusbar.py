import time

import customtkinter as ctk


class StatusBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.vector = None
        self.status = ctk.CTkLabel(self, text="Vector is waiting to connect with you.")
        self.status.grid(row=0, column=0, padx=10, sticky="ew")

    def connect_vector(self, robot):
        self.vector = robot

    def tracking_status(self):
        print(self.vector.status.are_motors_moving)
        if self.vector.status.is_animating:
            print("Vector is animating.")
            self.status.configure(text="Vector is animating.")
        elif self.vector.status.is_picked_up:
            print("Vector is picked up.")
            self.status.configure(text="Vector is picked up.")
        elif self.vector.status.are_motors_moving:
            print("Vector is moving.")
            self.status.configure(text="Vector is moving.")
        elif self.vector.status.is_charging:
            print("Vector is currently charging.")
            self.status.configure(text="Vector is currently charging.")
        elif self.vector.status.is_in_calm_power_mode:
            print("Vector is sleeping")
            self.status.configure(text="Vector is sleeping.")
        else:
            self.status.configure(text="Vector is chilling.")



