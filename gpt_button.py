import asyncio
import threading

import customtkinter as ctk

from chat_gpt import ChatGPT


class GPTButton(ctk.CTkButton):
    def __init__(self, master, *args, text, command, state):
        super().__init__(master, *args, text=text, command=command, state=state)
        self.entry = None
        self.question = None
        self.loop = asyncio.get_event_loop()
        self.gpt = ChatGPT()
        self.vector = None
        self.command = command

    def get_gpt_for_vector_speech(self):
        self.configure(state='disabled', command=None)
        self.question = self.entry.get(0.00, ctk.END)
        threading.Thread(target=self.async_thread).start()

    # Runs async thread
    def async_thread(self):
        self.loop.run_until_complete(self.create_task())

    # Creates an asyncio task and adds a callback function
    async def create_task(self):
        task = asyncio.create_task(self.send_to_gtp())
        task.add_done_callback(self.callback)
        await task

    # Allows user to press the generate button after task is complete
    def callback(self, task):
        self.configure(state='normal', command=self.command)
        self.entry.delete(0.0, ctk.END)

    async def send_to_gtp(self):
        response = self.gpt.ask_gpt(self.question)
        self.vector.behavior.say_text(response, use_vector_voice=False)

    def set_vector(self, vector, entry):
        self.vector = vector
        self.entry = entry
