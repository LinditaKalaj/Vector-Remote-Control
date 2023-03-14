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
        self.lift_speed = None
        self.pressed = {}
        self.move_speed = 100
        self.head_speed = 1.0
        self.video = None
        self.vector = robot
        self.configure_style()
        self.video = ctk.CTkLabel(self, text="")
        self.video.pack(fill=ctk.BOTH, expand=True)
        self.clear_text = ctk.CTkButton(self, text="Clear text", command=lambda: self.speak_entry.delete(0, ctk.END))
        self.speak_entry = ctk.CTkEntry(self, placeholder_text="Enter what you want Vector to say here!")
        self.clear_text.pack(fill=ctk.BOTH, expand=True)
        self.speak_entry.pack(fill=ctk.BOTH, expand=True)
        self.vector.camera.init_camera_feed()
        self.start_camera()
        self.set_binding()
        self.move()

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

    def set_binding(self):
        self.video.bind("<Button-1>", lambda event: self.video.focus())
        self.speak_entry.bind("<Return>", lambda event: self.vector_speak())
        self.bind("<KeyPress-w>", self.key_pressed)
        self.bind("<KeyRelease-w>", self.key_released)
        self.bind("<KeyPress-s>", self.key_pressed)
        self.bind("<KeyRelease-s>", self.key_released)
        self.bind("<KeyPress-a>", self.key_pressed)
        self.bind("<KeyRelease-a>", self.key_released)
        self.bind("<KeyPress-d>", self.key_pressed)
        self.bind("<KeyRelease-d>", self.key_released)
        self.pressed["w"] = False
        self.pressed["s"] = False
        self.pressed["a"] = False
        self.pressed["d"] = False

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

    def move(self):
        if self.pressed["w"] and self.pressed["a"]:
            self.vector.motors.set_wheel_motors(self.move_speed//2, self.move_speed)
        elif self.pressed["w"] and self.pressed["d"]:
            self.vector.motors.set_wheel_motors(self.move_speed, self.move_speed//2)
        elif self.pressed["s"] and self.pressed["a"]:
            self.vector.motors.set_wheel_motors(-(self.move_speed//2), -self.move_speed)
        elif self.pressed["s"] and self.pressed["d"]:
            self.vector.motors.set_wheel_motors(-self.move_speed, -(self.move_speed//2))
        elif self.pressed["w"]:
            self.vector.motors.set_wheel_motors(self.move_speed, self.move_speed)
        elif self.pressed["a"]:
            self.vector.motors.set_wheel_motors(-self.move_speed, self.move_speed)
        elif self.pressed["d"]:
            self.vector.motors.set_wheel_motors(self.move_speed, -self.move_speed)
        elif self.pressed["s"]:
            self.vector.motors.set_wheel_motors(-self.move_speed, -self.move_speed)
        self.after(100, self.move)

    def key_pressed(self, event):
        self.pressed[event.keysym] = True

    def key_released(self, event):
        self.pressed[event.char] = False
        if not(self.pressed["w"] or self.pressed["s"] or self.pressed["a"] or self.pressed["d"]):
            self.vector.motors.set_wheel_motors(0, 0)
