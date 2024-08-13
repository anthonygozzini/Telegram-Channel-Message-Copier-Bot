
# Telegram Channel Message Copier and Auto-Messenger Bot

## Overview

This Python script is a Telegram bot that performs two main functions:

1. **Automatic Messaging:** Sends a predefined message to a list of specified Telegram channels at regular intervals.
2. **Message Copying:** Copies messages from one channel and replicates them to other specified channels based on predefined rules.

This bot is built using the `python-telegram-bot` library and is intended to be run as a long-running process.

## Features

- **Automated Messaging:** Sends a message to all specified channels at intervals (configured to run every 21 hours).
- **Message Replication:** When a message is posted in a monitored channel, it is automatically copied to other target channels based on predefined rules.

## Requirements

- Python 3.7+
- `python-telegram-bot` library
- `python-dotenv` library

## Setup

Clone the Repository:

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

Install Dependencies:

```sh
pip install -r requirements.txt
```

Environment Variables:

Create a `.env` file in the root directory of the project and define the following environment variables:

```env
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
AUTO_MESSAGE_LINK=https://your-link.com
CHANNELS=channel_name_1:channel_id_1,channel_name_2:channel_id_2,...
```

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
- `AUTO_MESSAGE_LINK`: The message or link you want to auto-send to the channels.
- `CHANNELS`: A comma-separated list of channel names and their corresponding IDs in the format `name:id`.

## Running the Bot

To start the bot, simply run:

```sh
python your_script.py
```

The bot will start listening for messages and auto-send messages at the specified intervals.

## Logging

The bot uses Python's logging module to log important events and errors. Logs are printed to the console, and the log level can be adjusted as needed.

## License

This project is licensed under the MIT License.
