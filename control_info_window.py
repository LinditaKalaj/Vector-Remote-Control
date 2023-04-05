import customtkinter as ctk
from PIL import Image


class ControlInfoWindow(ctk.CTkToplevel):
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
        self.configure_style()
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
    
    def configure_style(self):
        self.configure(background='#303030')
        self.title("Vector's Control Info")
        ctk.set_default_color_theme("green")

        # Set min and max sizes
        height = 300
        width = 450
        self.minsize(450, 300)
        self.maxsize(450, 300)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        # Centers window based on users monitor
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))