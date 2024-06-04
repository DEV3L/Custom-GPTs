from loguru import logger
from trello import Card
from trello import List as TrelloList

from src.dataclasses.categorized_list import CategorizedLists
from src.dataclasses.trello_card import TrelloCard


def extract_card_info(trello_list: TrelloList, card: Card) -> TrelloCard:
    logger.debug(f"Extracting Trello Card information for card: {card.name}")
    return TrelloCard(
        list_name=trello_list.name,
        title=card.name,
        description=card.description,
        labels=[label.name for label in card.labels],
        comments=[comment["data"]["text"] for comment in card.comments],
        due_date=card.due_date,
    )


def trello_list_reducer(accumulator: CategorizedLists, trello_list: TrelloList) -> CategorizedLists:
    if trello_list.name in ["Backlog","Epics", "Icebox", "Questions"]:
        accumulator.planning.append(trello_list)
    elif trello_list.name in ["To Do"]:
        accumulator.todo.append(trello_list)
    elif trello_list.name in ["Doing"]:
        accumulator.doing.append(trello_list)
    elif trello_list.name in ["Team"]:
        accumulator.team.append(trello_list)
    else:
        accumulator.done.append(trello_list)
    return accumulator
