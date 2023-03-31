import customtkinter as ctk

from chat_gpt import ChatGPT


class GPTButton(ctk.CTkButton):
    def __init__(self, master, *args, text, command):
        super().__init__(master, *args, text=text, command=command)
        self.gpt = ChatGPT()

    def get_gpt_for_vector_speech(self, question):
        return self.gpt.ask_gpt(question)
