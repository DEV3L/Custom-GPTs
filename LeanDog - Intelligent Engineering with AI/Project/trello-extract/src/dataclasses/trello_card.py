from dataclasses import dataclass
from datetime import datetime
from typing import List, Literal


@dataclass
class TrelloCard:
    title: str
    list_name: str
    description: str
    labels: List[str]
    comments: List[str]
    due_date: datetime | Literal[""]
