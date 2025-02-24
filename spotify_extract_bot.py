import os
import yt_dlp
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from moviepy.editor import AudioFileClip
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, CallbackContext
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from keys.env
load_dotenv("keys.env")

# Set up Spotify API
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_AUTH_MANAGER = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=SPOTIPY_AUTH_MANAGER)

# Set up Telegram bot
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DOWNLOAD_PATH = "downloads/"

# Ensure the downloads directory exists
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

async def extract_song_details(spotify_url):
    """Extract song name and artist from a Spotify link."""
    track_id = spotify_url.split("/")[-1].split("?")[0]
    track_info = sp.track(track_id)
    song_name = track_info["name"]
    artist_name = track_info["artists"][0]["name"]
    return f"{song_name} {artist_name}"

async def download_song(query):
    """Download song using yt-dlp and convert to MP3 using moviepy."""
    temp_audio_path = f"{DOWNLOAD_PATH}/{query}.webm"  
    output_mp3_path = f"{DOWNLOAD_PATH}/{query}.mp3"  

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": temp_audio_path,  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{query}"])

    # Convert the downloaded file to MP3 using moviepy
    audio_clip = AudioFileClip(temp_audio_path)
    audio_clip.write_audiofile(output_mp3_path, codec="mp3", bitrate="192k")
    audio_clip.close()

    os.remove(temp_audio_path)

    return output_mp3_path

async def handle_message(update: Update, context: CallbackContext):
    """Handle incoming messages with Spotify links."""
    spotify_url = update.message.text
    if "spotify.com/track" not in spotify_url:
        await update.message.reply_text("Please send a valid Spotify track link.")
        return

    await update.message.reply_text("Fetching song details...")
    song_query = await extract_song_details(spotify_url)

    await update.message.reply_text(f"Searching for: {song_query}")
    file_path = await download_song(song_query)

    await update.message.reply_text("Uploading the file...")
    with open(file_path, "rb") as audio:
        await update.message.reply_audio(audio, title=song_query)

    os.remove(file_path)  # Clean up after sending

async def start(update: Update, context: CallbackContext):
    """Respond to /start command."""
    await update.message.reply_text("Send me a Spotify song link, and I'll fetch the MP3 for you!")

def main():
    """Start the bot."""
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
