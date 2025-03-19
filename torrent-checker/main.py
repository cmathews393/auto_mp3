"""Main script for detecting and processing new FLAC torrents."""

import time
from pathlib import Path

from config import qbit_config
from qbittorrent import QBitTorrentClient


def check_new_torrents():
    """Check for new completed torrents and process them."""
    qb = QBitTorrentClient(qbit_config)

    while True:
        completed_torrents = qb.get_completed_torrents()

        flac_torrents = {
            torrent["name"]: Path(torrent["content_path"])
            for torrent in completed_torrents
            if qb.is_flac_available(torrent["hash"])
        }

        if flac_torrents:
            print("FLAC torrents found:", flac_torrents)

        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    check_new_torrents()
