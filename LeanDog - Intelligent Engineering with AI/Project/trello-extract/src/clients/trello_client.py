from trello import TrelloClient

from src.settings import Settings


def get_trello_client(settings: Settings) -> TrelloClient:
    return TrelloClient(
        api_key=settings.trello_api_key,
        api_secret=settings.trello_api_token,
    )
