"""Configuration settings for the auto_mp3 script."""

import os

import dotenv

API_KEY = "your_api_key_here"
ORPHEUS_UPLOAD_URL = "https://orpheus.example.com/upload"
FLAC_DIRECTORY = "/path/to/flac/files"
MP3_DIRECTORY = "/path/to/mp3/files"
TORRENT_CLIENT_URL = "http://localhost:8080"
TORRENT_CLIENT_USERNAME = "username"
TORRENT_CLIENT_PASSWORD = "password"
CHECK_INTERVAL = 60  # in seconds

dotenv.load_dotenv()
orpheus_key = os.getenv("ORPHEUS_TOKEN")
qbit_config = {
    "port": os.getenv("QBIT_PORT"),
    "host": os.getenv("QBIT_HOST"),
}
