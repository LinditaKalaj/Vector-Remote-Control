import asyncio
import threading
import time

import anki_vector
import customtkinter as ctk
import multiprocessing as mp
import sys

from PIL import ImageTk


class Window(ctk.CTk):
    def __init__(self, robot):
        super().__init__()
        self.video = None
        self.vector = robot
        self.configure_style()
        self.video = ctk.CTkLabel(self, text="")
        self.video.pack(fill=ctk.BOTH, expand=True)
        self.video.bind("<Button-1>", lambda event: self.video.focus())
        self.clear_text = ctk.CTkButton(self, text="Clear text", command=lambda: self.speak_entry.delete(0, ctk.END))
        self.speak_entry = ctk.CTkEntry(self, placeholder_text="Enter what you want Vector to say here!")
        self.clear_text.pack(fill=ctk.BOTH, expand=True)
        self.speak_entry.pack(fill=ctk.BOTH, expand=True)
        self.vector.camera.init_camera_feed()
        self.start_camera()
        self.speak_entry.bind("<Return>", lambda event: robot.behavior.say_text(self.speak_entry.get()))
        self.bind("<KeyPress-Up>", self.up_arrow)
        self.bind("<KeyRelease-Up>", self.stop)
        self.bind("<KeyPress-Down>", self.down_arrow)
        self.bind("<KeyRelease-Down>", self.stop)
        self.bind("<KeyPress-Left>", self.left_arrow)
        self.bind("<KeyRelease-Left>", self.stop)
        self.bind("<KeyPress-Right>", self.right_arrow)
        self.bind("<KeyRelease-Right>", self.stop)
    def configure_style(self):
        self.configure(background='#303030')
        self.title("Vector Remote")
        ctk.set_default_color_theme("green")

        # Set min and max sizes
        height = 500
        width = 700
        self.minsize(700, 500)
        self.maxsize(700, 500)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        # Centers window based on users monitor
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    # LOADS SO SLOW- LOOK AT IT LATER
    def start_camera(self):
        image = self.vector.camera.latest_image.raw_image
        photo_image = ctk.CTkImage(light_image=image, size=(453, 339))
        self.video.configure(image=photo_image)
        self.after(20, self.start_camera)

    # Vectors speech
    def vector_speak(self):
        to_say = self.speak_entry.get()
        if to_say == "":
            return
        self.vector.behavior.say_text(to_say)

    def up_arrow(self, x):
        print("Up arrow pressed")
        self.vector.motors.set_wheel_motors(300, 300)

    def left_arrow(self, x):
        print("Left arrow pressed")
        self.vector.motors.set_wheel_motors(-300, 300)

    def right_arrow(self, x):
        print("Right arrow pressed")
        self.vector.motors.set_wheel_motors(300, -300)

    def down_arrow(self, x):
        print("Down arrow pressed")
        self.vector.motors.set_wheel_motors(-300, -300)

    def stop(self, x):
        self.vector.motors.set_wheel_motors(0, 0)
