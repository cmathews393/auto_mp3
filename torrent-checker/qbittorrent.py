"""Client for interacting with qBittorrent."""

import qbittorrentapi
import qbittorrentapi.torrents


class QBitTorrentClient:
    """Client for interacting with qBittorrent."""

    def __init__(
        self: "QBitTorrentClient",
        connection_info: dict[str, str | int],
    ) -> None:
        """Initialize the qBittorrent client."""
        self.client = qbittorrentapi.Client(
            **connection_info,
        )
        self.client.auth_log_in()

    def get_completed_torrents(self) -> qbittorrentapi.torrents.TorrentInfoList:
        """Get a list of completed torrents."""
        return self.client.torrents_info(
            status_filter="completed,seeding",
            category="lidarr-imported",
            SIMPLE_RESPONSES=True,
        )

    def get_torrent_metadata(
        self,
        torrent_hash: str,
    ) -> qbittorrentapi.torrents.TorrentInfoList:
        """Get metadata for a specific torrent."""
        return self.client.torrents_info(torrent_hashes=torrent_hash)

    def is_flac_available(self, torrent_hash: str) -> bool:
        """Check if a FLAC file is available in the torrent."""
        metadata = self.get_torrent_metadata(torrent_hash)

        return any(file.name.endswith(".flac") for file in metadata[0].files)

    def close(self) -> None:
        """Logout from the qBittorrent client."""
        self.client.auth_log_out()
