
from utils import convert_text_to_html
from aria_dialog_api_base import AriaDialogAPI

class Team_ARIADialogAPI(AriaDialogAPI):
    def OpenConnection(self, auth=None):
        return True
    def CloseConnection(self):
        return True
    def StartSession(self):
        return True
    def GetResponse(self, text):
        htmltext = convert_text_to_html(text)
        return {'success': True,
                'response': htmltext}