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
        self.label = ctk.CTkLabel(self)
        self.label.pack(fill=ctk.BOTH, expand=True)
        self.vector.camera.init_camera_feed()
        self.start_camera()

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

    # LOADS SO SLOW- LOOK AT IT LATER
    def start_camera(self):
        image = self.vector.camera.latest_image
        raw_img = image.raw_image
        print(raw_img)
        photo_image = ctk.CTkImage(light_image=raw_img, size=(320, 240))
        self.label.configure(image=photo_image)
        self.after(1, self.start_camera)
