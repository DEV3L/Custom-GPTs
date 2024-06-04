from datetime import datetime
from typing import Literal

from src.dataclasses.categorized_list import CategorizedLists
from src.dataclasses.trello_card import TrelloCard
from src.formatters.generate_markdown import generate_markdown


def test_headers():
    expected_markdown = """# PLANNING

# TODO

# DOING

# DONE

# USERS

# TEAM
"""

    categorized_list = CategorizedLists(
        planning=[build_trello_card()],
        todo=[build_trello_card()],
        doing=[build_trello_card()],
        done=[build_trello_card()],
        users=[build_trello_card()],
        team=[build_trello_card()],
    )

    markdown = generate_markdown(categorized_list)

    assert markdown == expected_markdown


def test_card_list_names():
    expected_markdown = """# TODO

## List Name

Task 1

## List Name

Task 2
"""

    categorized_list = CategorizedLists(
        todo=[
            build_trello_card(list_name="Task 1"),
            build_trello_card(list_name="Task 2"),
        ]
    )

    markdown = generate_markdown(categorized_list)

    assert markdown == expected_markdown


def test_card_title_names():
    expected_markdown = """# TODO

## Title

Title 1

## Title

Title 2
"""

    categorized_list = CategorizedLists(
        todo=[
            build_trello_card(title="Title 1"),
            build_trello_card(title="Title 2"),
        ]
    )

    markdown = generate_markdown(categorized_list)

    assert markdown == expected_markdown


def test_card_labels():
    expected_markdown = """# TODO

## List Name

Task 1

## Labels

- bug
- urgent
"""

    categorized_list = CategorizedLists(
        todo=[
            build_trello_card(list_name="Task 1", labels=["bug", "urgent"]),
        ]
    )

    markdown = generate_markdown(categorized_list)

    assert markdown == expected_markdown


def test_card_due_date():
    expected_markdown = """# TODO

## List Name

Task 1

## Due Date

2024-05-01 00:00:00
"""

    categorized_list = CategorizedLists(
        todo=[
            build_trello_card(
                list_name="Task 1",
                due_date=datetime(2024, 5, 1, 0, 0),
            ),
        ]
    )

    markdown = generate_markdown(categorized_list)

    assert markdown == expected_markdown


def test_card_descriptions():
    expected_markdown = """# TODO

## List Name

Task 1

## Description

Description of task 1

## List Name

Task 2

## Description

### Description of task 2
"""

    categorized_list = CategorizedLists(
        todo=[
            build_trello_card(list_name="Task 1", description="Description of task 1"),
            build_trello_card(list_name="Task 2", description="# Description of task 2"),
        ]
    )

    markdown = generate_markdown(categorized_list)

    assert markdown == expected_markdown


def test_card_comments():
    expected_markdown = """# TODO

## List Name

Task 1

## Comments

- - -

Comment 1
"""

    categorized_list = CategorizedLists(
        todo=[
            build_trello_card(list_name="Task 1", comments=["---", "Comment 1"]),
        ]
    )

    markdown = generate_markdown(categorized_list)

    assert markdown == expected_markdown


def test_generate_markdown():
    expected_markdown = """# TODO

## Title

Title 1

## List Name

Task 1

## Labels

- bug
- urgent

## Due Date

2024-05-01 00:00:00

## Description

Description of task 1

## Comments

Comment 1
"""

    categorized_list = CategorizedLists(
        todo=[
            build_trello_card(
                title="Title 1",
                list_name="Task 1",
                labels=["bug", "urgent"],
                due_date=datetime(2024, 5, 1, 0, 0),
                description="Description of task 1",
                comments=["Comment 1"],
            ),
        ]
    )

    markdown = generate_markdown(categorized_list)

    assert markdown == expected_markdown


def build_trello_card(
    *,
    title="",
    list_name="",
    description="",
    labels: list[str] = [],
    comments: list[str] = [],
    due_date: datetime | Literal[""] = "",
):
    return TrelloCard(
        title=title,
        list_name=list_name,
        description=description,
        labels=labels,
        comments=comments,
        due_date=due_date,
    )
