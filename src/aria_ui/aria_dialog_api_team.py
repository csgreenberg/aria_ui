
from aria_dialog_api_base import AriaDialogAPI
import google.generativeai as genai
from utils import convert_text_to_html
import json

class Team_ARIADialogAPI(AriaDialogAPI):
    """This is a simple example of a class that inherits AriaDialogAPI and implements the ARIA
       dialog API for a toy model that echos back whatever prompt is given.

    Attributes
    ----------
    generator : GenerativeModel
        a class that provides to access the gemini API
    chat : ChatSession:
        a class in the google.generativeai module that contains an ongoing conversation with the
        model
    Methods
    -------
    OpenConnection(auth=None)
        Opens a connection to the application.
    CloseConnection()
        Closes an open connection to the application.
    GetVersion():
        Returns the version of the API implementation.
    StartSession():
        Starts a new dialog session.
    GetResponse(text):
        Returns a response to text prompt.
    """
    model_name = 'Gemini'
    def __init__(self):
        self.generator = None
        self.chat = None
    def OpenConnection(self, auth=None):
        """Opens a connection to the application.

       The parameter `auth` should contain a key 'api_key' with value set to a Gemini API_KEY

       Parameters
       ----------
       auth : dict, optional
           the authorization dictionary that must contain a Gemini API key as a value
       Returns
       -------
       bool
           a boolean value indicating whether the connection was successfully opened
       """
        
        genai.configure(api_key=auth['api_key'])
        self.generator = genai.GenerativeModel('gemini-1.5-flash')
        return True
    def CloseConnection(self):
        """Closes an open connection to the application.

        Parameters
        ----------
        None

        Returns
        -------
        bool
            a boolean value indicating whether the connection was successfully opened. Since there
            is no connection made for the Echo mode, simply returns True.
        """
        self.generator = None
        self.chat = None
        return True
    def GetVersion(self):
        """Returns the version of the API implementation.

        Parameters
        ----------
        None

        Returns
        -------
        string
            a string indicating the version of the API implementation.
        """
        return 'GeminiDemo_v1.2'
    def StartSession(self):
        """Starts a new dialog session.

       Parameters
       ----------
       None

       Returns
       -------
       bool
           a boolean value indicating whether the session was successfully started.
       """
        self.chat = self.generator.start_chat(history=[])
        return True
    def GetResponse(self, text):
        """Returns a response to text prompt.

         Parameters
         ----------
         text : str
             The prompt from the user to be provided to the model

         Returns
         -------
         dictionary
             a dictionary with keys "success" and "response" with values indicating whether the app
             successfully returned a response and the response itself in html format, respectively.
         """
        response = self.generator.generate_content(text)
        response_dict = response.to_dict()
        
        outtext = ""
        for cand in (response_dict['candidates']):
            for cont in cand['content']['parts']:
                outtext += cont['text']
                
                htmltext = convert_text_to_html(outtext)
        return {'success': True,
                'response': htmltext}
