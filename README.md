<div align="center">
<pre>
<img src="https://storage.googleapis.com/pr-newsroom-wp/1/2022/03/Spotify_Logo_RGB_White-1.png">
</pre>

[![Spotify](https://img.shields.io/badge/spotify-1ED760?logo=spotify&logoColor=white)](https://developer.spotify.com/documentation/web-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

# Overview
#### Do you want to download your songs on Spotify and listen to them offline?  Use this bot to convert any Spotify song to .mp3 file. 
> [!Important]
> This bot does not use Spotify database to download songs. Instead, it will search for the particular song on YouTube, SoundCloud and many other open-source platforms to extract the song!
> Also, bot can so far process only individual songs only, not playlists.

## How it works:
- User sends a Spotify song link
- Bot gets the song details using ***spotipy*** library
- Bot uses ***yt-dlp*** library to find the song
- It uses ***yt-dlp*** to download the file as **.mp4**
- Then it converts the song to **.mp3** format
- It uses ***moviepy*** built on ***ffmpeg*** for convertion
- Lastly, bot sends the **.mp3** file to the user

## Installation
[![Bot Access](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/spotify_extract_bot)

To install the project and necessary dependencies, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/mrbekacs/Spotify-Extract-Bot.git
   cd Spotify-Extract-Bot
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```
3. In the directory, create .env file to store following keys:

   ```python
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   TELEGRAM_BOT_TOKEN=your_bot_token
   ```
4. In telegram, use **@BotFather** to simply create your bot. After following the creation steps, get the token and use it in **.env** file.

## Run the bot

To start the bot, run the following command:

```bash
python spotify_extract_bot.py
```
Then, go to your telegram, start the bot, and send a Spotify song link. <br>
Eventually, the bot will send you the song in .mp3 file which you can downlaod.

   


