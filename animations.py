import customtkinter as ctk


class Animations(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.option_menu_var = None
        self.configure(height=50)
        self.configure_cols()
        self.vector = None
        self.anim_trigger_names = None

        self.greet = ctk.CTkButton(self, text="٩(＾◡＾)۶")
        self.frustrated = ctk.CTkButton(self, text="（◞‸◟）")
        self.huh = ctk.CTkButton(self, text="(º～º)")
        self.owo_sad = ctk.CTkButton(self, text="(◕︵◕)")
        self.ring = ctk.CTkButton(self, text="(ﾉ･_-)☆")
        self.sleepy = ctk.CTkButton(self, text="(ꈍ .̮ ꈍ)")
        self.hehe = ctk.CTkButton(self, text="(*´∀`*)")
        self.woa = ctk.CTkButton(self, text="(ʘᆽʘ)")
        self.all = ctk.CTkOptionMenu(self)
        self.greet.grid(row=0, column=0)
        self.frustrated.grid(row=0, column=1)
        self.huh.grid(row=0, column=2)
        self.owo_sad.grid(row=0, column=3)
        self.ring.grid(row=0, column=4)
        self.sleepy.grid(row=0, column=5)
        self.hehe.grid(row=0, column=6)
        self.woa.grid(row=0, column=7)
        self.all.grid(row=0, column=8, columnspan=2)

    def set_vector(self, robot):
        self.vector = robot
        self.anim_trigger_names = self.vector.anim.anim_trigger_list
        self.option_menu_var = ctk.StringVar(value=self.anim_trigger_names[0])
        self.all.configure(values=self.anim_trigger_names, command=self.option_menu_callback, variable=self.option_menu_var)
        self.greet.configure(command=lambda: self.vector.anim.play_animation_trigger("GreetAfterLongTime"))
        self.frustrated.configure(command=lambda: self.vector.anim.play_animation_trigger("FrustratedByFailureMajor"))
        self.huh.configure(command=lambda: self.vector.anim.play_animation_trigger("AudioOnlyHuh"))
        self.owo_sad.configure(command=lambda: self.vector.anim.play_animation_trigger("Feedback_MeanWords"))
        self.ring.configure(command=lambda: self.vector.anim.play_animation_trigger("TimerRing"))
        self.sleepy.configure(command=lambda: self.vector.anim.play_animation_trigger("ReactToGoodNight"))
        self.hehe.configure(command=lambda: self.vector.anim.play_animation_trigger("PounceSuccess"))
        self.woa.configure(command=lambda: self.vector.anim.play_animation_trigger("ObservingLookUp"))
        # self.greetings.configure(command=lambda: self.vector.anim.play_animation_trigger("ObservingLookUp"))

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
        self.grid_columnconfigure(9, weight=1)

    def option_menu_callback(self, x):
        print(self.option_menu_var)
        print(x)
        self.vector.anim.play_animation_trigger(self.option_menu_var)


