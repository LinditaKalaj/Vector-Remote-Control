import tkinter as tk
import customtkinter as ctk


class MenuBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.init_file_menu()
        self.init_help_menu()

    def init_file_menu(self):
        file = tk.Menubutton(self, text='File', background='gray17', foreground='gray81', activeforeground='gray98',
                             activebackground='#2CC985', borderwidth=0)
        file_menu = tk.Menu(file, tearoff=0, borderwidth=0)
        file_menu.config(borderwidth=0, activeborderwidth=0, bd=0)
        file_menu.add_command(label='GPT API Key', background='gray17', foreground='gray81', activeforeground='gray98',
                              activebackground='#2CC985')
        file_menu.add_separator(background='gray17')
        file_menu.add_command(label='Quit', background='gray17', foreground='gray81', activeforeground='gray98',
                              activebackground='#2CC985')
        file.config(menu=file_menu, borderwidth=0)
        file.pack(side='left', pady=1)

    def init_help_menu(self):
        help_button = tk.Menubutton(self, text='Help', background='gray17', foreground='gray81',
                                    activeforeground='gray98', activebackground='#2CC985')
        help_menu = tk.Menu(help_button, tearoff=0)
        help_menu.add_command(label='Controls', background='gray17', foreground='gray81', activeforeground='gray98',
                              activebackground='#2CC985')
        help_button.config(menu=help_menu)
        help_button.pack(side='left', pady=1)
