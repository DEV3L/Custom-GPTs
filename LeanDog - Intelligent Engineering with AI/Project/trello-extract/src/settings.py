import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    trello_api_key: str
    trello_api_token: str
    trello_board_name: str

    def __init__(self):
        self.trello_api_key = os.getenv("TRELLO_API_KEY", "")
        self.trello_api_token = os.getenv("TRELLO_API_TOKEN", "")
        self.trello_board_name = os.getenv("TRELLO_BOARD_NAME", "")


def get_settings() -> Settings:
    return Settings()
