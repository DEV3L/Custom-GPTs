# Trello Extract

Trello Extract is a Python project that uses the `py-trello` library and `python-dotenv` to authenticate with the Trello API and fetch details from Trello boards, lists, and cards. This project demonstrates how to securely manage API credentials and interact with Trello's API to retrieve project data for further processing.

## Features

- Authenticate with the Trello API using OAuth.
- Fetch details of all accessible Trello boards.
- Retrieve lists and cards from a specified Trello board.
- Securely manage API credentials using environment variables.

## Requirements

- Python 3.11+

## Setup

### Step 1: Register for Trello API Access

1. **Sign Up for a Trello Account**:

   - If you don't have a Trello account, sign up at [Trello](https://trello.com/).

2. **Get API Key and Token**:
   - Go to the [Trello Developer Portal](https://trello.com/app-key).
   - Copy your API Key.
   - Click on the "Token" link to generate a token. This token will be used for authentication in your API requests.

### Step 2: Install Necessary Python Packages

1. Setup a virtual environment with dependencies and activate it:

```bash
brew install hatch
hatch env create
hatch shell
```

### Step 3: Configure Environment Variables

1. Copy the env.local file to a new file named .env

```bash
cp env.local .env
```

2. Update `.env` file with your Trello API credentials:

```
TRELLO_API_KEY=TRELLO_API_KEY
TRELLO_API_TOKEN=TRELLO_API_TOKEN
TRELLO_BOARD_NAME=Intelligent Engineering with AI (.NET)
```

### Step 4: Run the Script

Run the script to authenticate and fetch data from your Trello board:

```bash
python trello_integration.py
```

## Usage

The `trello_integration.py` script will:

1. Authenticate with the Trello API using the credentials provided in the `.env` file.
2. Fetch and print the details of all accessible Trello boards.
3. Fetch and print the lists and cards from the first Trello board in the list.

### Example Output

```
# TODO

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
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to improve this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
