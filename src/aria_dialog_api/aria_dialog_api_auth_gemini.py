
from aria_dialog_api_base import AriaDialogAPI

import google.generativeai as genai

class AuthGemini_ARIADialogAPI(AriaDialogAPI):
    def __init__(self):
        self.generator = None
        self.chat = None
    def OpenSession(self, auth):
        if not self.generator:
            genai.configure(api_key=auth['api_key'])
            self.generator = genai.GenerativeModel('gemini-1.5-flash')
        self.chat = self.generator.start_chat(history=[])
    def CloseSession(self, destroy_generator=False):
        if destroy_generator:
            self.generator = None
            self.chat = None
        else:
            self.chat = self.generator.start_chat(history=[])
    def GetResponse(self, text):
        response = self.chat.send_message(text, stream=True)
        text = ''
        for chunk in response:
            text += chunk.text
        return text