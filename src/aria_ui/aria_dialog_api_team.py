
from utils import convert_text_to_html
from aria_dialog_api_base import AriaDialogAPI

class Team_ARIADialogAPI(AriaDialogAPI):
    """This is a simple example of a class that inherits AriaDialogAPI and implements the ARIA
    dialog API for a toy model that echos back whatever prompt is given."""
    model_name = 'Echo'
    def OpenConnection(self, auth=None):
        """Opens a connection to the application.

        The parameter `auth` is ignored.

        Parameters
        ----------
        auth : dict, optional
            the authorization dictionary that, for example, might contain an API key as a value;
            since there is no authorization needed for the Echo model, the parameter is ignored.
        Returns
        -------
        bool
            a boolean value indicating whether the connection was successfully opened; since there
            is no connection made for the Echo mode, simply returns True.
        """
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
        return True
    @staticmethod
    def GetVersion():
        """Returns the version of the API implementation.

        Parameters
        ----------
        None

        Returns
        -------
        string
            a string indicating the version of the API implementation.
        """
        return '0.1'
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
        htmltext = convert_text_to_html(text)
        return {'success': True,
                'response': htmltext}