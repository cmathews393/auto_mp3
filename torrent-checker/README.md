# Torrent Checker

## Overview
Torrent Checker is a Python application designed to monitor completed torrents and convert FLAC files to MP3 format at 320kbps. The application checks if a torrent is in FLAC format and ensures that it does not already have a FLAC version before proceeding with the conversion and re-uploading to the Orpheus platform.

## Project Structure
```
torrent-checker
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── orpheus.py
│   ├── lame.py
│   ├── qbittorrent.py
│   └── config.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/torrent-checker.git
   ```
2. Navigate to the project directory:
   ```
   cd torrent-checker
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Configure your settings in `src/config.py`, including API keys and file paths.
2. Run the application:
   ```
   python src/main.py
   ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.