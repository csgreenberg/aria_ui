from aria_dialog_api_base import AriaDialogAPI

from llama import Llama
from llama import Dialog
from llama.generation import Message
from typing import List

class LocalLlama_ARIADialogAPI(AriaDialogAPI):
    def __init__(self, ckpt_dir='llama-2-7b-chat/', tokenizer_path='tokenizer.model'):
        self.ckpt_dir = ckpt_dir
        self.tokenizer_path = tokenizer_path
        self.generator = None
        self.dialog = []
    def OpenSession(self, auth=None):
        if not self.generator:
            generator = Llama.build(
                ckpt_dir=self.ckpt_dir,
                tokenizer_path=self.tokenizer_path)
            self.generator = generator
        self.dialog = []
    def CloseSession(self, destroy_generator=False):
        if destroy_generator:
            self.generator = None
        self.dialog = []
    def GetResponse(self, text):
        self.dialog.append(Message(role='user', content=text))
        dialogs = [self.dialog]
        results = self.generator.chat_completion(dialogs=dialogs)
        result = results[0]
        print(type(result))
        self.dialog.append(result)
        return result['content']