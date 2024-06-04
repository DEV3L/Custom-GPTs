from functools import reduce

from loguru import logger
from trello import Board, TrelloClient
from trello import List as TrelloList

from src.dataclasses.categorized_list import CategorizedLists
from src.dataclasses.trello_card import TrelloCard
from src.functions import first
from src.services.trello_utilities import extract_card_info, trello_list_reducer


def extract_card_info_from_list(trello_list: list[TrelloList]) -> list[TrelloCard]:
    return [extract_card_info(trello_list, card) for trello_list in trello_list for card in trello_list.list_cards()]


class TrelloService:
    def __init__(self, client: TrelloClient):
        self.client = client

    def extract_cards_info(self, board: Board):
        categorized_lists = self.categorize_lists(board)

        logger.debug(f"Extracting Trello Cards from categorized lists: {categorized_lists}")

        planning = extract_card_info_from_list(categorized_lists.planning)
        todo = extract_card_info_from_list(categorized_lists.todo)
        doing = extract_card_info_from_list(categorized_lists.doing)
        done = extract_card_info_from_list(categorized_lists.done)
        users = extract_card_info_from_list(categorized_lists.users)
        team = extract_card_info_from_list(categorized_lists.team)

        return CategorizedLists(planning=planning, todo=todo, doing=doing, done=done, users=users, team=team)

    def categorize_lists(self, board: Board) -> CategorizedLists[TrelloList]:
        trello_lists = self.get_lists_for_board(board)
        filtered_trello_lists = filter(lambda trello_list: "_" != trello_list.name, trello_lists)
        return reduce(
            trello_list_reducer,
            filtered_trello_lists,
            CategorizedLists[TrelloList](planning=[], todo=[], doing=[], done=[], users=[], team=[]),
        )

    def get_board_by_name(self, board_name: str) -> Board:
        boards = self._list_boards()
        board = first(filter(lambda board: board.name == board_name, boards))

        if not board:
            raise RuntimeError(f"Board with name '{board_name}' not found.")

        return board

    def get_lists_for_board(self, board: Board) -> list[TrelloList]:
        logger.debug(f"Listing Trello Lists for board: {board.name}")
        return board.all_lists()

    def _list_boards(self) -> list[Board]:
        logger.debug("Listing Trello Boards")
        return self.client.list_boards()
