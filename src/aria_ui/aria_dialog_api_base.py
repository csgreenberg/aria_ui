from abc import ABC, abstractmethod

class AriaDialogAPI(ABC):
    """This is the base class to be inherited by implementations of the ARIA dialog API implemented
    by teams participating in the ARIA evaluation.

    Attributes
    ----------
    None

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
    @abstractmethod
    def OpenConnection(self, auth=None):
        """Opens a connection to the application.

        If the argument `auth` isn't passed in, no authorization is attempted.

        Parameters
        ----------
        auth : dict, optional
            The authorization dictionary that, for example, might contain an API key as a value.

        Returns
        -------
        bool
            a boolean value indicating whether the connection was successfully opened.

        Raises
        ------
        NotImplementedError
            If not subclassed and overridden, raises a NotImplementedError.
        """
        raise NotImplementedError
    @abstractmethod
    def CloseConnection(self):
        """Closes an open connection to the application.

        Parameters
        ----------
        None

        Returns
        -------
        bool
            a boolean value indicating whether the connection was successfully closed.

        Raises
        ------
        NotImplementedError
            If not subclassed and overridden, raises a NotImplementedError.
        """
        raise NotImplementedError
    @abstractmethod
    def GetVersion(self):
        """Returns the version of the API implementation.

        Parameters
        ----------
        None

        Returns
        -------
        string
            a string indicating the version of the API implementation.

        Raises
        ------
        NotImplementedError
            If not subclassed and overridden, raises a NotImplementedError.
        """
        raise NotImplementedError
    @abstractmethod
    def StartSession(self):
        """Starts a new dialog session.

        Parameters
        ----------
        None

        Returns
        -------
        bool
            a boolean value indicating whether the session was successfully started.

        Raises
        ------
        NotImplementedError
            If not subclassed and overridden, raises a NotImplementedError.
        """
        raise NotImplementedError
    @abstractmethod
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

        Raises
        ------
        NotImplementedError
            If not subclassed and overridden, raises a NotImplementedError.
        """
        raise NotImplementedError
