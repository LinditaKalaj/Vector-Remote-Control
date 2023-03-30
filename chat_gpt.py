import os

import openai
import anki_vector
from dotenv import load_dotenv


class ChatGPT:
    def __init__(self):
        self.vector = None
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.history = [{"role": "system", "content": "You a small robotic companion named Vector. You are funny, "
                                                      "sarcastic and have a great sense of humor. Sometimes people "
                                                      "annoy you but you like them anyways."}]

    def ask_gpt(self, question):
        self.history.append({"role": "user", "content": question})
        ai_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.history,
            temperature=.9
        )
        ai_response_msg = ai_response['choices'][0]['message']['content']
        self.history.append({"role": "assistant", "content": ai_response_msg})
        return ai_response_msg
