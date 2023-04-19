import asyncio
import threading
import customtkinter as ctk
from chat_gpt import ChatGPT


class GPTButton(ctk.CTkButton):
    """
    A custom tkinter button class that deals with gpt questions

    Attributes
    ----------
    entry: object
        pointer to entry box in gui
    question: str
        question the user wants to ask gpt
    gpt: object
        gpt class to handle the question
    vector: object
        pointer to vector
    command: function
        the function that gets called when gpt button is clicked
        (used for disabling and enabling when gpt thread starts and completes)

    Methods
    -------
    get_gpt_for_vector_speech(question)
        Disables button and starts thread
    create_task()
        creates task and adds callback function to previous method
    callback()
        Allows user to press the generate button after task is complete
    send_to_gtp()
        Sends question to gpt, receives a response and makes Vector speak
    set_vector()
        After successful connection, set_vector gets called to get object pointers

    """
    def __init__(self, master, *args, text, command, state):
        super().__init__(master, *args, text=text, command=command, state=state)
        self.entry = None
        self.question = None
        self.loop = asyncio.get_event_loop()
        self.gpt = ChatGPT()
        self.vector = None
        self.command = command

    def get_gpt_for_vector_speech(self, question):
        """sends question to gpt class

        Parameters
        ----------
        question : str
            question or comment asked by the user
        Returns
        -------
        None
        """
        self.configure(state='disabled', command=None)
        self.question = question
        threading.Thread(target=self.loop.run_until_complete(self.create_task())).start()

    async def create_task(self):
        task = asyncio.create_task(self.send_to_gtp())
        task.add_done_callback(self.callback)
        await task

    def callback(self, task):
        self.configure(state='normal', command=self.command)
        self.entry.delete(0.0, ctk.END)

    async def send_to_gtp(self):
        response = self.gpt.ask_gpt(self.question)
        self.vector.behavior.say_text(response, use_vector_voice=False)

    def set_vector(self, vector, entry):
        self.vector = vector
        self.entry = entry
