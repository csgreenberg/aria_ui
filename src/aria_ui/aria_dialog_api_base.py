from abc import ABC, abstractmethod

class AriaDialogAPI(ABC):
    @abstractmethod
    def OpenSession(auth=None):
        raise NotImplementedError

    @abstractmethod
    def CloseSession():
        raise NotImplementedError

    @abstractmethod
    def GetResponse(text):
        raise NotImplementedError


