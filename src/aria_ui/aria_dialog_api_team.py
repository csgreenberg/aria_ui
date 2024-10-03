from utils import convert_text_to_html
from aria_dialog_api_base import AriaDialogAPI

# Groq/Llama implementation specific imports
from groq import Groq
import random
from langchain.chains import ConversationChain, LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

class Team_ARIADialogAPI(AriaDialogAPI):
    """This is a simple example of a class that inherits AriaDialogAPI and implements the Groq
    API for the Llama3 LLM."""
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
        self.groq_api_key = auth['api_key']  # Replace 'your_api' with your actual API key
        self.model_name= "llama3-8b-8192"
        return self.groq_api_key
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
        self.groq_chat = None
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
        return self.model_name
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
        conversational_memory_length = 100
        self.memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)
        # Initialize Groq Langchain chat object and conversation
        self.groq_chat = ChatGroq(
            groq_api_key=self.groq_api_key, 
            model_name=self.model_name,
            streaming=True
        )
        if self.groq_chat is not None:
            return True
        else:
            return False
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
             successfully returned a response and the response itself in text or markdown text format, respectively.
         """
        # Construct a chat prompt template using various components
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=""
                ),  # This is the persistent system prompt that is always included at the start of the chat.

                MessagesPlaceholder(
                    variable_name="chat_history"
                ),  

                HumanMessagePromptTemplate.from_template(
                    "{text}"
                ),  # This template is where the user's current input will be injected into the prompt.
            ]
        )

        # Create a conversation chain using the LangChain LLM (Language Learning Model)
        conversation = LLMChain(
            llm=self.groq_chat,  # The Groq LangChain chat object initialized earlier.
            prompt=prompt,  # The constructed prompt template.
            verbose=True,   # Enables verbose output, which can be useful for debugging.
            memory=self.memory,  # The conversational memory object that stores and manages the conversation history.
        )

        response_text = conversation.predict(text=text)

        if response_text is not None:
            success = True
        else:
            success = False

        return {'success': True,
                'response': response_text}
