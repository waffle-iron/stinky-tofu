from linebot import LineBotApi
from linebot.exceptions import LineBotApiError

from core.model.situation.abc_situation import Situation


class AskingWhoSitu(Situation):
    TYPE_ASKING_WHO = 'TYPE_ASKING_WHO'

    def __init__(self, user_id, api: LineBotApi) -> None:
        super().__init__()
        self.api = api
        self.user_id = user_id
        self.keywords = ['我是誰']

    def get_message_type(self) -> str:
        return AskingWhoSitu.TYPE_ASKING_WHO

    def get_response(self):

        try:
            profile = self.api.get_profile(self.user_id)
            return "你是" + profile.display_name + "啊～"
        except LineBotApiError as e:
            return '我還不認識你～ \n 點這個連結讓我們成為好友吧 \n'

    def __contains__(self, text):
        if type(text) is not str:
            raise TypeError

        return any(keyword in text.lower() for keyword in self.keywords)