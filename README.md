# Football Team Info Bot

A Python-based Telegram bot that provides information about football teams using TheSportsDB API.

## Features

- **Team Information**: Get details about football teams including country, manager, stadium, and description
- **Simple Commands**: Easy-to-use command interface
- **Logo Links**: Direct links to team logos
- **Error Handling**: Basic error handling and logging

## Prerequisites

Before running this bot, you need:

- Python 3.7 or higher
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- A free API key from [TheSportsDB](https://www.thesportsdb.com/)

## Installation

1. **Clone or download this project**

2. **Install required dependencies**:
   ```bash
   pip install python-telegram-bot requests
   ```

3. **Configure your credentials**:
   
   Open `bot.py` and replace the placeholder values:
   
   ```python
   # Replace with your actual credentials
   TOKEN = 'your_telegram_bot_token_here'  # From @BotFather
   API_KEY = 'your_sportsdb_api_key_here'  # From TheSportsDB
   ```

## Getting Your Credentials

### Telegram Bot Token
1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Use `/newbot` command
3. Follow the instructions to create your bot
4. Copy the generated token

### TheSportsDB API Key
1. Register at [TheSportsDB](https://www.thesportsdb.com/)
2. Get your free API key from your account dashboard
3. Replace the placeholder API key in the code

## Usage

### Running the Bot
```bash
python bot.py
```

The bot will start and begin polling for messages. Keep the terminal open to keep the bot running.

### Available Commands
- `/start` - Initialize the bot and welcome message
- `/help` - Show available commands and usage
- `/team [team name]` - Get information about a specific team

### Examples
```
/team Arsenal
/team Real Madrid
/team Barcelona
/team "Bayern Munich"
```

## Project Structure

```
.
├── main.py          # Main bot application
└── README.md       # This documentation
```

## API Reference

This bot uses the [TheSportsDB API](https://www.thesportsdb.com/) to fetch football team data. The free tier has rate limits, so extensive use may require API plan upgrades.

## Limitations

- Free API tier has request limitations
- Team data depends on TheSportsDB database completeness
- No persistent storage implemented (stateless operation)
- Basic error handling only

## Troubleshooting

### Logs
The bot outputs logs to the console with timestamps and error messages for debugging.



---

**Note**: Remember to create your own bot through @BotFather and replace the placeholder credentials before running the code.
