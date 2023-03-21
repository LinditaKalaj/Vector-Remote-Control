from tkinter import ttk
import tkinter as tk

import customtkinter as ctk


class Animations(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.style = None
        self.greet = None
        self.frustrated = None
        self.owo_sad = None
        self.ring = None
        self.sleepy = None
        self.hehe = None
        self.woa = None
        self.all = None
        self.option_menu_var = None
        self.configure_cols()
        self.vector = None
        self.anim_trigger_names = None

        self.attach_buttons()

    def set_vector(self, robot):
        self.vector = robot
        self.anim_trigger_names = robot.anim.anim_trigger_list
        self.attach_listeners()

    def configure_cols(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure(7, weight=1)
        self.grid_columnconfigure(8, weight=1)

    def combo_callback(self, selected):
        self.vector.anim.play_animation_trigger(self.all.get())

    def attach_listeners(self):
        if self.anim_trigger_names is not None:
            self.all.config(values=self.anim_trigger_names, height=20)
            self.all.bind("<<ComboboxSelected>>", self.combo_callback)
        self.greet.configure(command=lambda: self.vector.anim.play_animation_trigger("GreetAfterLongTime"))
        self.frustrated.configure(command=lambda: self.vector.anim.play_animation_trigger("FrustratedByFailureMajor"))
        self.owo_sad.configure(command=lambda: self.vector.anim.play_animation_trigger("Feedback_MeanWords"))
        self.ring.configure(command=lambda: self.vector.anim.play_animation_trigger("TimerRing"))
        self.sleepy.configure(command=lambda: self.vector.anim.play_animation_trigger("ReactToGoodNight"))
        self.hehe.configure(command=lambda: self.vector.anim.play_animation_trigger("PounceSuccess"))
        self.woa.configure(command=lambda: self.vector.anim.play_animation_trigger("ObservingLookUp"))

    def attach_buttons(self):
        self.greet = ctk.CTkButton(self, text="(＾◡＾)", width=10)
        self.frustrated = ctk.CTkButton(self, text="（◞‸◟）", width=10)
        self.owo_sad = ctk.CTkButton(self, text="(◕︵◕)", width=10)
        self.ring = ctk.CTkButton(self, text="(ﾉ･_-)☆", width=10)
        self.sleepy = ctk.CTkButton(self, text="(ꈍ .̮ ꈍ)", width=10)
        self.hehe = ctk.CTkButton(self, text="(*´∀`*)", width=10)
        self.woa = ctk.CTkButton(self, text="(ʘᆽʘ)", width=10)
        combostyle = ttk.Style()
        combostyle.theme_use("clam")
        combostyle.configure('ARD.TCombobox', background="green", fieldbackground="lightgreen")
        self.all = ttk.Combobox(self, values=["Loading..."], style='ARD.TCombobox')
        self.greet.grid(row=0, column=0)
        self.frustrated.grid(row=0, column=1)
        self.owo_sad.grid(row=0, column=2)
        self.ring.grid(row=0, column=3)
        self.sleepy.grid(row=0, column=4)
        self.hehe.grid(row=0, column=5)
        self.woa.grid(row=0, column=6)
        self.all.grid(row=0, column=7, columnspan=2)



