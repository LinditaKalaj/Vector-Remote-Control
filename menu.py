import sys
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
                              activebackground='#2CC985', command=self.open_gpt_api_dialog)
        file_menu.add_separator(background='gray17')
        file_menu.add_command(label='Quit', background='gray17', foreground='gray81', activeforeground='gray98',
                              activebackground='#2CC985', command=sys.exit)
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

    def open_gpt_api_dialog(self):
        width=300
        height=150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        dialog = ctk.CTkInputDialog(text="Paste in your GPT OpenAI api key here:", title="GPT OpenAI Api")
        dialog.geometry('%dx%d+%d+%d' % (width, height, x, y))
        dialog_input = dialog.get_input()
        if not dialog_input:
            return
        with open(".env", "w") as f:
            new_api = 'OPENAI_API_KEY=' + dialog_input
            f.write(new_api)
