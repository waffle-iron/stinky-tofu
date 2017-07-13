from core.model.situation.abc_situation import Situation


class EchoSitu(Situation):
    TYPE_ECHO = "TYPE_ECHO"
    DEFAULT_RESPONSE = '不好意思請問你要我說什麼呢？'

    def __init__(self) -> None:
        super().__init__()
        self.keywords = ['說', '重複']
        self.context = EchoSitu.DEFAULT_RESPONSE

    def get_response(self, text=""):
        self.context = EchoSitu.DEFAULT_RESPONSE

        sp = text.split(" ", 1)

        if len(sp) > 1 and len(sp[1].strip()) > 0:
            self.context = sp[1]
        return self.context

    def __contains__(self, text):
        if type(text) is not str:
            raise TypeError

        sp = text.split(" ", 1)
        command = sp[0]

        if any(keyword in command.lower() for keyword in self.keywords):
            return True
        else:
            return False

    def get_message_type(self) -> str:
        return EchoSitu.TYPE_ECHO
