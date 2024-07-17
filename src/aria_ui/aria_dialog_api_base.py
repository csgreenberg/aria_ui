from abc import ABC, abstractmethod

class AriaDialogAPI(ABC):
    @abstractmethod
    def OpenConnection(auth=None):
        raise NotImplementedError
    @abstractmethod
    def CloseConnection():
        raise NotImplementedError
    @abstractmethod
    def StartSession():
        raise NotImplementedError
    @abstractmethod
    def GetResponse(text):
        raise NotImplementedError


