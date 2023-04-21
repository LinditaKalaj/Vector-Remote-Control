import customtkinter as ctk
from PIL import Image

from window_utils import Utils


class ControlInfoWindow(ctk.CTkToplevel):
    """
    Class used to display a window with control information for vector.

    Attributes
    ----------

    self.arrow_img_holder: object
        ctk label used to show an image of keyboard arrows
    self.wsad_img_holder: object
        ctk label used to show an image of the "wsad" keys
    self.arrow_info_txt: object
        Text information about vectors movements using the arrow keys
    self.wsad_info_txt: object
        Text information about vectors movements using the "wsad" keys
    self.arrow_info_frame: object
        Frame that wraps around the text information for the arrow keys
    self.wsad_info_frame: object
        Frame that wraps around the text information for the "wsad" keys
    self.arrow_img: object
        image of the keyboard arrows
    self.wsad_img: object
        image of the wsad keys
    self.win_utils: object
        class that configures the window style

    Methods
    -------
    get_keyboard_button_imgs(self)
        gets local images (the arrow keys and wsad key images.
    init_items(self)
        loads the image into the label with text information wrapped in a frame
    add_items_to_grid(self)
        adds the label with the image and text information to the window
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arrow_img_holder = None
        self.wsad_img_holder = None
        self.arrow_info_txt = None
        self.wsad_info_txt = None
        self.arrow_info_frame = None
        self.wsad_info_frame = None
        self.arrow_img = None
        self.wsad_img = None
        self.win_utils = Utils(self)
        self.win_utils.configure_style("Vector's Control Info", 450, 300)
        self.get_keyboard_button_imgs()
        self.init_items()
        self.add_items_to_grid()

    def get_keyboard_button_imgs(self):
        self.wsad_img = ctk.CTkImage(light_image=Image.open("./assets/wsad_transparent.png"), size=(224, 148))
        self.arrow_img = ctk.CTkImage(light_image=Image.open("./assets/arrow_transparent.png"), size=(224, 148))
        
    def init_items(self):
        self.wsad_info_frame = ctk.CTkFrame(self)
        self.arrow_info_frame = ctk.CTkFrame(self)
        
        self.wsad_info_txt = ctk.CTkLabel(self.wsad_info_frame,
                                          text="Use WSAD keys to move Vector. W for up, S for down, A for left, "
                                               "and D for right.", wraplength=150) 
        self.arrow_info_txt = ctk.CTkLabel(self.arrow_info_frame, text="Use the UP and DOWN arrow to control Vector's "
                                                                       "Lift. The RIGHT and LEFT arrows are used to "
                                                                       "control his head.", wraplength=150) 
        self.wsad_img_holder = ctk.CTkLabel(self, image=self.wsad_img, text="")

        self.arrow_img_holder = ctk.CTkLabel(self, image=self.arrow_img, text="")
        
    def add_items_to_grid(self):
        self.wsad_info_txt.pack(padx=10, pady=10)
        self.arrow_info_txt.pack(padx=10, pady=10)
        self.wsad_img_holder.grid(row=0, column=0)
        self.arrow_img_holder.grid(row=1, column=0)
        self.wsad_info_frame.grid(row=0, column=1, padx=10, pady=10)
        self.arrow_info_frame.grid(row=1, column=1, padx=10, pady=10)
