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

## How it works:
- User sends a Spotify song link
- Bot gets the song details using ***spotipy*** library
- Bot uses ***yt-dlp*** library to find the song
- It uses ***yt-dlp*** to download the file as **.mp4**
- Then it converts the song to **.mp3** format
- It uses ***moviepy*** built on ***ffmpeg*** for convertion
- Lastly, bot sends the **.mp3** file to the user

## Installation
