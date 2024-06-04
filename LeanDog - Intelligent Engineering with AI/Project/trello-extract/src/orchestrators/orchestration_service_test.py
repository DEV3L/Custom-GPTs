import os
from unittest.mock import MagicMock, patch

from trello import Board

from src.dataclasses.categorized_list import CategorizedLists
from src.dataclasses.trello_card import TrelloCard
from src.orchestrators.orchestration_service import OrchestrationService
from src.services.trello_service import TrelloService


def test_get_board_markdown(mock_board: Board, trello_card: TrelloCard):
    expected_markdown = """# TODO

## Title

Title

## List Name

To Do

## Labels

- Label1
- Label2

## Description

Test card description

## Comments

Test comment
"""

    mock_trello_service = MagicMock(spec=TrelloService)
    mock_trello_service.get_board_by_name.return_value = mock_board
    mock_trello_service.extract_cards_info.return_value = CategorizedLists(todo=[trello_card])

    orchestration_service = OrchestrationService(mock_trello_service)
    markdown = orchestration_service.get_board_markdown("Test Board")

    assert markdown == expected_markdown

    mock_trello_service.get_board_by_name.assert_called_once_with("Test Board")
    mock_trello_service.extract_cards_info.assert_called_once_with(mock_trello_service.get_board_by_name.return_value)


@patch("src.orchestrators.orchestration_service.generate_markdown")
def test_write_board_markdown_to_file(mock_generate_markdown, tmpdir):
    mock_generate_markdown.return_value = "# Mock Markdown Content"

    mock_trello_service = MagicMock(spec=TrelloService)
    mock_trello_service.get_board_by_name.return_value = "mock_board"
    mock_trello_service.extract_cards_info.return_value = "mock_cards_info"

    orchestration_service = OrchestrationService(trello_service=mock_trello_service)

    board_name = "TestBoard"
    directory = tmpdir.mkdir("markdown_files")
    file_path = os.path.join(directory, f"{board_name} Trello.txt")

    result_path = orchestration_service.write_board_markdown_to_file(board_name, str(directory))

    assert result_path == file_path
    with open(result_path, "r") as file:
        content = file.read()
    assert content == "# Mock Markdown Content"
