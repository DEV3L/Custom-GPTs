from unittest.mock import MagicMock, patch

from src.clients.trello_client import get_trello_client
from src.settings import get_settings


@patch("src.clients.trello_client.TrelloClient")
def test_get_trello_client(trello_client: MagicMock) -> None:
    settings = get_settings()
    settings.trello_api_key = "123"
    settings.trello_api_token = "456"

    client = get_trello_client(settings)

    trello_client.assert_called_once_with(
        api_key=settings.trello_api_key,
        api_secret=settings.trello_api_token,
    )

    assert client == trello_client()
