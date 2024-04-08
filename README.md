# Deforum Daily Papers Bot

Deforum Daily Papers Bot is a Discord bot that fetches the latest AI research papers from the Hugging Face Papers API and sends them to designated channels in your Discord server.

## Features

- Automatically fetches the latest AI research papers every minute
- Sends paper details (title, URL, and media) as an embedded message in Discord
- Allows server administrators to set the channel for receiving daily papers using the `/setchannel` command

## Installation

1. Clone the repository:
`https://github.com/blueangel1313/DeforumDailyPapers.git`

2. Install the required dependencies:
`pip install -r requirements.txt`

3. Create a `.env` file in the project directory with the following content:
`HFREADME=your_hugging_face_api_key
DISCORDKEY=your_discord_bot_token`

Replace `your_hugging_face_api_key` with your Hugging Face API key and `your_discord_bot_token` with your Discord bot token.

4. Run the bot:
`python bot.py`

## Usage

- Invite the bot to your Discord server.
- Use the `/setchannel` command to set the channel where the bot will send daily papers.
- The bot will automatically fetch and send the latest AI research papers every minute.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
