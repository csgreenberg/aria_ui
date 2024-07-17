
from aria_dialog_api_base import AriaDialogAPI
import google.generativeai as genai
from utils import convert_text_to_html

class Team_ARIADialogAPI(AriaDialogAPI):
    def __init__(self):
        self.generator = None
        self.chat = None
    def OpenConnection(self, auth=None):
        genai.configure(api_key=auth['api_key'])
        self.generator = genai.GenerativeModel('gemini-1.5-flash')
        return True
    def CloseConnection(self):
        self.generator = None
        self.chat = None
        return True
    def StartSession(self):
        self.chat = self.generator.start_chat(history=[])
        return True
    def GetResponse(self, text):
        response = self.chat.send_message(text, stream=True)
        text = ''
        for chunk in response:
            text += chunk.text
        htmltext = convert_text_to_html(text)
        return {'success': True,
                'response': htmltext}