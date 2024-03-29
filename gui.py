import asyncio
import threading
import customtkinter as ctk
from tkinter import messagebox
import anki_vector
from PIL import Image
from anki_vector import util
from anki_vector.exceptions import VectorConnectionException, VectorNotFoundException, VectorConfigurationException, \
    VectorControlTimeoutException
from animations import Animations
from gpt_button import GPTButton
from move_vector import MoveVector
from speed import Speed
from statusbar import StatusBar
from volume import Volume
import anki_vector.events
from window_utils import Utils


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme("green")
        self.vector = None  # Connection to Vectors SDK
        self.win_utils = Utils(self)  # Window styling utils
        self.win_utils.configure_style("Vector Remote", 900, 700)
        self.win_utils.configure_grid(7, 4)
        self.move_vector = None  # Class used for Vectors movements
        self.gpt_button = None
        self.say_text_button = None
        self.vector_status = None  # Frame class containing Vectors status
        self.speed = None  # Frame class containing Vectors speed controls
        self.volume = None  # Frame class containing Vectors Volume controls
        self.start_video = False
        self.animations = None  # Frame class containing Vectors Animation controls
        self.blank_photo_image = None
        self.greet_button = None
        self.connection_status = None
        self.connect_button = None
        self.speak_entry = None
        self.clear_text = None
        self.video = None
        self.loop = asyncio.get_event_loop()  # Async loop to allow free movement of gui while vector connects
        self.configure_items()

    """
    Inits Classes and buttons and places them on a grid
    :returns None
    """
    def configure_items(self):
        self.vector_status = StatusBar(self)
        self.vector_status.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10)

        self.connect_button = ctk.CTkButton(self, text="Connect", command=lambda: self.initialize_vector_connection())
        self.connect_button.grid(row=1, column=4, columnspan=1, padx=10,  sticky="e")

        self.connection_status = ctk.CTkLabel(self, text="Status: Disconnected")
        self.connection_status.grid(row=1, column=3, sticky="e")

        self.volume = Volume(self)
        self.volume.grid(row=2, column=0, columnspan=3, sticky="sew", padx=(30, 0))

        self.speed = Speed(self)
        self.speed.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=(10, 0), padx=(30, 0))

        self.video = ctk.CTkLabel(self, text="")
        self.blank_photo_image = ctk.CTkImage(light_image=Image.open("./assets/blank_camera.png"), size=(453, 339))
        self.video.configure(image=self.blank_photo_image)
        self.video.grid(row=2, column=3, columnspan=3, rowspan=3, sticky=" ew")

        self.animations = Animations(master=self)
        self.animations.grid(row=5, column=0, columnspan=4, padx=(20, 0), sticky="sew")

        self.clear_text = ctk.CTkButton(self, text="Clear text", command=lambda: self.speak_entry.delete(0.0, ctk.END))
        self.clear_text.grid(row=5, column=4, columnspan=1, sticky="se", pady=0, padx=(0, 20))

        self.speak_entry = ctk.CTkTextbox(self, height=100, state="disabled")
        self.speak_entry.grid(row=6, column=0, columnspan=4, rowspan=2, sticky="nsew", padx=10, pady=(10, 10))

        self.say_text_button = ctk.CTkButton(self, text="Say text", command=self.vector_speak)
        self.say_text_button.grid(row=6, column=4, sticky="nsew", padx=10, pady=10)

        self.gpt_button = GPTButton(self, text="GPT Button", command=self.send_entry_to_gpt, state='normal')
        self.gpt_button.grid(row=7, column=4, sticky="nsew", padx=10, pady=10)

    """
    Sets button bindings: 
    Video binding was used to focus out of entry box.
    Return binding used when text in entry box needs to be sent to Vectors speech.
    Focus in and out events used to disable Vectors movements when typing.
    :returns None
    """
    def set_binding(self):
        self.video.bind("<Button-1>", lambda event: self.video.focus())
        self.speak_entry.bind("<Return>", lambda event: self.vector_speak())
        self.speak_entry.bind("<FocusIn>", lambda event: self.unbind_movement_bindings())
        self.speak_entry.bind("<FocusOut>", lambda event: self.set_movement_bindings())
        self.set_movement_bindings()

    """
    Sets directional bindings using wsad and binds them to functions in move_vector class
    :returns None
    """
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

    """
    Unbinds movement when focused in entry box, called from the focusin entry binding event
    :returns None
    """
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

    """
    Grabs picture feed from Vector and updates self.video. 
    Then registers a callback function on its self for continuous video feed.
    :returns: None
    """
    def start_camera(self):
        if self.start_video:
            image = self.vector.camera.latest_image.raw_image
            photo_image = ctk.CTkImage(light_image=image, size=(453, 339))
            self.video.configure(image=photo_image)
            self.after(20, self.start_camera)

    """
    Grabs picture feed from Vector and updates self.video. 
    Then registers a callback function on its self for continuous video feed.
    :param: None
    :returns: 'break' so there is no new line created by enter
    :rtype: string
    """
    def vector_speak(self):
        to_say = self.speak_entry.get(0.00, ctk.END)
        if to_say == "":
            return 'break'
        self.vector.behavior.say_text(to_say)
        self.speak_entry.delete(0.0, ctk.END)
        return 'break'

    """
    Registers a callback function to run main_move function from vectors move class
    :returns: None
    """
    def move(self):
        self.move_vector.main_move()
        self.after(100, self.move)

    """
    Registers a callback function to continuously get vectors tracking status
    :returns: None
    """
    def update_status(self):
        self.vector_status.tracking_status()
        self.after(100, self.update_status)

    """
    Starts a thread to connect to Vector asynchronously
    :returns: None
    """
    def initialize_vector_connection(self):
        self.connect_button.configure(state="disabled", command=None)
        threading.Thread(target=self.loop.run_until_complete(self.send_to_vector())).start()

    async def send_to_vector(self):
        task = asyncio.create_task(self.connect_to_vector())
        task.add_done_callback(self.callback)
        await task

    """
    Async function to connect to vector. If an error occurs, an error message will be displayed to the user. 
    If no errors occurred then vector will initialize along with his camera feed and functionality.
    :returns: None
    """
    async def connect_to_vector(self):
        args = util.parse_command_args()
        try:
            self.vector = anki_vector.AsyncRobot(args.serial,
                                                 behavior_activation_timeout=30.0,
                                                 cache_animation_lists=False)
            self.vector.connect()

        except VectorNotFoundException:
            messagebox.showerror('Error!', "Unknown error has occurred.")
        except VectorConnectionException:
            messagebox.showwarning('Warning!', "Vector's animations have failed to load. Animations may not function "
                                               "properly. Please try reconnecting Vector to resolve the issue.")
        except VectorConfigurationException:
            messagebox.showerror('Error!', "Could not find the sdk configuration file. Please run ezVector Setup "
                                           "prior to opening this program.")
        except VectorControlTimeoutException:
            messagebox.showerror('Error!', "Failed to get control of Vector. Please verify that Vector is connected "
                                           "to the internet, is on a flat surface, and is fully charged.")

        else:
            if self.vector:
                self.start_video = True
                self.vector.camera.init_camera_feed()
                self.start_camera()
                self.move_vector = MoveVector(self.vector)
                self.set_binding()
                self.move()
                self.connection_status.configure(text="Status: Connected")
                self.animations.set_vector(self.vector)
                self.volume.set_vector(self.vector)
                self.speed.set_move(self.move_vector)
                self.vector_status.connect_vector(self.vector)
                self.gpt_button.set_vector(self.vector, self.speak_entry)
                self.update_status()
                self.speak_entry.configure(state="normal")

    """
    Replaces the connect button with a disconnect if Vector is properly connected.
    Else, the button changes states from disabled to normal.
    :returns: None
    """
    def callback(self, task):
        if self.vector:
            self.connect_button = ctk.CTkButton(self, state="normal", text="Disconnect",
                                                command=lambda: self.disconnect_vector())
            self.connect_button.grid(row=1, column=4, columnspan=1, padx=10, sticky="e")
        else:
            self.connect_button = ctk.CTkButton(self, text="Connect", command=lambda: self.
                                                initialize_vector_connection())
            self.connect_button.grid(row=1, column=4, columnspan=1, padx=10, sticky="e")

    """
    When the disconnect button is pressed, the video callback function stops and all movement will unbind. 
    The connect button will reappear to grant the user an opportunity to connect again.
    :returns: None
    """
    def disconnect_vector(self):
        if not self.vector:
            return
        self.start_video = False
        self.unbind_movement_bindings()
        self.connect_button.configure(state="disabled", command=None)
        self.video.configure(image=self.blank_photo_image)
        self.vector.disconnect()
        self.connection_status.configure(text="Status: Disconnected")
        self.connect_button = ctk.CTkButton(self, text="Connect", command=lambda: self.initialize_vector_connection())
        self.connect_button.grid(row=1, column=4, columnspan=1, padx=10, sticky="e")

    """
    Calls gpt button function to send user input to gpt class to process the question and make vector say the response.
    :returns: None
    """
    def send_entry_to_gpt(self):
        self.gpt_button.get_gpt_for_vector_speech(self.speak_entry.get(0.0, ctk.END))
        self.speak_entry.delete(0.0, ctk.END)
