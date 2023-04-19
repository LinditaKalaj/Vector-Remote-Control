import os
import openai
from dotenv import load_dotenv


class ChatGPT:
    """
    Class used to connect to gpt and send questions

    Attributes
    ----------

    self.vector: object
        Vectors object to utilize his sdk

    self.history: str
        Chat log saved so gpt knows the whole scope of the convo. Added first prompt to get Vector in character

    Methods
    -------
    ask_gpt(self, question)
        Sends gpt the question or comment the user typed in the entry box
    """

    def __init__(self):
        self.vector = None

        # load api key from .env file
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

        self.history = [{"role": "system", "content": "You a small robotic companion named Vector. You are funny, "
                                                      "sarcastic and have a great sense of humor. Sometimes people "
                                                      "annoy you but you like them anyways."}]

    def ask_gpt(self, question):
        """
        Appends the question to history, sends it to gpt and receives a response.

        :param question: str, The question being sent to gpt
        :return: str, gpt response to the question asked
        """

        self.history.append({"role": "user", "content": question})
        ai_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.history,
            temperature=.9
        )
        ai_response_msg = ai_response['choices'][0]['message']['content']
        self.history.append({"role": "assistant", "content": ai_response_msg})
        return ai_response_msg
