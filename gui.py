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
        self.label = None
        self.height = None
        self.width = None
        self.vector = robot
        self.loop = asyncio.get_event_loop()
        self.configure_style()
        self.label = ctk.CTkLabel(self, text="")
        self.label.pack(fill=ctk.BOTH, expand=True)
        self.speak_entry = ctk.CTkEntry(self, placeholder_text="Enter what you want Vector to say here!")
        self.speak_entry.pack(fill=ctk.BOTH, expand=True)
        self.vector.camera.init_camera_feed()
        self.start_camera()
        self.speak_entry.bind("<Return>", lambda event: robot.behavior.say_text(self.speak_entry.get()))

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
        print(image)
        photo_image = ctk.CTkImage(light_image=image, size=(453, 339))
        self.label.configure(image=photo_image)
        self.after(20, self.start_camera)

    # Vectors speech
    def vector_speak(self):
        to_say = self.speak_entry.get()
        if to_say == "":
            return
        self.vector.behavior.say_text(to_say)
