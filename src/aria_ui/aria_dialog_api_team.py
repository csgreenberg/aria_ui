
from utils import convert_text_to_html
from aria_dialog_api_base import AriaDialogAPI

class Team_ARIADialogAPI(AriaDialogAPI):
    model_name = 'Echo'
    def OpenConnection(self, auth=None):
        return True
    def CloseConnection(self):
        return True
    @staticmethod
    def GetVersion():
        return '0.1'
    def StartSession(self):
        return True
    def GetResponse(self, text):
        htmltext = convert_text_to_html(text)
        return {'success': True,
                'response': htmltext}