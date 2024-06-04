from dotenv import load_dotenv
from loguru import logger

from src.clients.trello_client import get_trello_client
from src.orchestrators.orchestration_service import OrchestrationService
from src.services.trello_service import TrelloService
from src.settings import get_settings

load_dotenv()


def main():
    settings = get_settings()
    orchestration_service = OrchestrationService(TrelloService(get_trello_client(settings)))

    try:
        markdown_file_name = orchestration_service.write_board_markdown_to_file(settings.trello_board_name, "bin")
        logger.info(f"Markdown file written to {markdown_file_name}")
    except RuntimeError as e:
        logger.error(e)


if __name__ == "__main__":
    main()
