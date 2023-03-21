# -*- coding: UTF-8 -*-
import asyncio
import threading

import customtkinter as ctk
from tkinter import messagebox
import anki_vector
from PIL import Image
from anki_vector import util
from anki_vector.exceptions import VectorConnectionException, VectorNotFoundException, VectorConfigurationException

from animations import Animations
from move_vector import MoveVector


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.start_video = False
        self.animations = None
        self.blank_photo_image = None
        self.animations_frame = None
        self.loop = asyncio.get_event_loop()
        self.greet_button = None
        self.frustrated_button = None
        self.connection_status = None
        self.connect_button = None
        self.speak_entry = None
        self.clear_text = None
        self.video = None
        self.vector = None
        self.move_vector = None
        self.configure_style()
        self.configure_grid()
        self.configure_items()
        # self.video = ctk.CTkLabel(self, text="")
        # self.video.pack(fill=ctk.BOTH, expand=True)
        # self.clear_text = ctk.CTkButton(self, text="Clear text", command=lambda: self.speak_entry.delete(0, ctk.END))
        # self.speak_entry = ctk.CTkEntry(self, placeholder_text="Enter what you want Vector to say here!")
        # self.clear_text.pack(fill=ctk.BOTH, expand=True)
        # self.speak_entry.pack(fill=ctk.BOTH, expand=True)
        # self.vector.camera.init_camera_feed()
        # self.start_camera()
        # self.set_binding()
        # self.move()

    def configure_style(self):
        self.configure(background='#303030')
        self.title("Vector Remote")
        ctk.set_default_color_theme("green")

        # Set min and max sizes
        height = 700
        width = 900
        self.minsize(900, 700)
        self.maxsize(900, 700)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        # Centers window based on users monitor
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def configure_grid(self):
        # Configures row and col weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def configure_items(self):
        self.connect_button = ctk.CTkButton(self, text="Connect", command=lambda: self.initialize_vector_connection())
        self.connect_button.grid(row=0, column=4, columnspan=1, padx=10,  sticky="e")
        self.connection_status = ctk.CTkLabel(self, text="Status: Disconnected")
        self.connection_status.grid(row=0, column=3, sticky="nsew")
        self.video = ctk.CTkLabel(self, text="")
        self.blank_photo_image = ctk.CTkImage(light_image=Image.open("./assets/blank_camera.png"), size=(453, 339))
        self.video.configure(image=self.blank_photo_image)
        self.video.grid(row=1, column=0, columnspan=5, rowspan=5, sticky="ew")

        self.animations = Animations(master=self)
        self.animations.grid(row=7, column=0, columnspan=4, rowspan=1, padx=10, sticky="ew")

        self.clear_text = ctk.CTkButton(self, text="Clear text", command=lambda: self.speak_entry.delete(0, ctk.END))
        self.clear_text.grid(row=7, column=4, columnspan=1, sticky="se", pady=17, padx=10)
        self.speak_entry = ctk.CTkEntry(self, placeholder_text="Enter what you want Vector to say here!")
        self.speak_entry.grid(row=8, column=0, columnspan=5, rowspan=1, sticky="nsew", padx=10)

    def set_binding(self):
        self.video.bind("<Button-1>", lambda event: self.video.focus())
        self.speak_entry.bind("<Return>", lambda event: self.vector_speak())
        self.speak_entry.bind("<FocusIn>", lambda event: self.unbind_movement_bindings())
        self.speak_entry.bind("<FocusOut>", lambda event: self.set_movement_bindings())
        self.set_movement_bindings()

    def set_movement_bindings(self):
        self.bind("<KeyPress-w>", self.move_vector.key_pressed)
        self.bind("<KeyRelease-w>", self.move_vector.key_released)
        self.bind("<KeyPress-s>", self.move_vector.key_pressed)
        self.bind("<KeyRelease-s>", self.move_vector.key_released)
        self.bind("<KeyPress-a>", self.move_vector.key_pressed)
        self.bind("<KeyRelease-a>", self.move_vector.key_released)
        self.bind("<KeyPress-d>", self.move_vector.key_pressed)
        self.bind("<KeyRelease-d>", self.move_vector.key_released)
        self.bind("<KeyPress-Up>", lambda event: self.move_vector.move_lift(1))
        self.bind("<KeyRelease-Up>", self.move_vector.stop_lift)
        self.bind("<KeyPress-Down>", lambda event: self.move_vector.move_lift(-1))
        self.bind("<KeyRelease-Down>", self.move_vector.stop_lift)
        self.bind("<KeyPress-Right>", lambda event: self.move_vector.move_head(1))
        self.bind("<KeyRelease-Right>", self.move_vector.stop_head)
        self.bind("<KeyPress-Left>", lambda event: self.move_vector.move_head(-1))
        self.bind("<KeyRelease-Left>", self.move_vector.stop_head)

    def unbind_movement_bindings(self):
        self.unbind("<KeyPress-w>")
        self.unbind("<KeyRelease-w>")
        self.unbind("<KeyPress-s>")
        self.unbind("<KeyRelease-s>")
        self.unbind("<KeyPress-a>")
        self.unbind("<KeyRelease-a>")
        self.unbind("<KeyPress-d>")
        self.unbind("<KeyRelease-d>")
        self.unbind("<KeyPress-Up>")
        self.unbind("<KeyRelease-Up>")
        self.unbind("<KeyPress-Down>")
        self.unbind("<KeyRelease-Down>")
        self.unbind("<KeyPress-Right>")
        self.unbind("<KeyRelease-Right>")
        self.unbind("<KeyPress-Left>")
        self.unbind("<KeyRelease-Left>")

    # LOADS SO SLOW- LOOK AT IT LATER
    def start_camera(self):
        if self.start_video:
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
        self.move_vector.main_move()
        self.after(100, self.move)

    def initialize_vector_connection(self):
        self.connect_button.configure(state="disabled", command=None)
        threading.Thread(target=self.async_thread).start()

    async def connect_to_vector(self):
        args = util.parse_command_args()
        try:
            self.vector = anki_vector.AsyncRobot(args.serial)
            self.vector.connect()
            anim_trigger_names = self.vector.anim.anim_trigger_list
            for anim_trigger_name in anim_trigger_names:
                print(anim_trigger_name)
        except VectorNotFoundException as v:
            print("1A connection error occurred: %s" % v)
        except VectorConnectionException as e:
            print("2A connection error occurred: %s" % e)
            messagebox.showwarning('Warning!', "Vector's animations have failed to load. Animations may not function "
                                               "properly. Please try reconnecting Vector to resolve the issue.")
        except VectorConfigurationException as config_e:
            messagebox.showerror('Error!', "Could not find the sdk configuration file. Please run ezVector Setup "
                                           "prior to opening this program.")
            print("3A connection error occurred: %s" % config_e)
        finally:
            if self.vector:
                self.start_video = True
                self.vector.camera.init_camera_feed()
                self.start_camera()
                self.move_vector = MoveVector(self.vector)
                self.set_binding()
                self.move()
                self.connection_status.configure(text="Status: Connected")
                self.animations.set_vector(self.vector)

    # Runs async thread
    def async_thread(self):
        self.loop.run_until_complete(self.send_to_vector())

    # Creates an asyncio task and adds a callback function
    async def send_to_vector(self):
        task = asyncio.create_task(self.connect_to_vector())
        task.add_done_callback(self.callback)
        await task

    # Allows user to press the generate button after task is complete
    def callback(self, task):
        if self.vector:
            self.connect_button = ctk.CTkButton(self, state="normal", text="Disconnect", command=lambda: self.disconnect_vector())
            self.connect_button.grid(row=0, column=4, columnspan=1, padx=10, sticky="e")
        else:
            self.connect_button = ctk.CTkButton(self, text="Connect", command=lambda: self.initialize_vector_connection())
            self.connect_button.grid(row=0, column=4, columnspan=1, padx=10, sticky="e")

    def disconnect_vector(self):
        self.start_video = False
        self.unbind_movement_bindings()
        self.connect_button.configure(state="disabled", command=None)
        self.video.configure(image=self.blank_photo_image)
        self.vector.disconnect()
        self.connection_status.configure(text="Status: Disconnected")
        self.connect_button = ctk.CTkButton(self, text="Connect", command=lambda: self.initialize_vector_connection())
        self.connect_button.grid(row=0, column=4, columnspan=1, padx=10, sticky="e")

