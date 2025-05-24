"""
Video management for VideoWall.
"""
import random
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer

from videowall.core.video_loader import VideoLoader
from videowall.config.settings import MAX_ACTIVE_PLAYERS

class VideoManager:
    """
    Manages video players and media content for VideoWall.
    """
    
    def __init__(self, video_wall, m3u8_links=None, local_videos=None):
        """
        Initialize the video manager.
        
        Args:
            video_wall (VideoWall): The parent VideoWall instance
            m3u8_links (list, optional): List of M3U8 stream URLs
            local_videos (list, optional): List of local video file paths
        """
        self.video_wall = video_wall
        self.tiles = video_wall.display_manager.tiles
        self.players = []
        self.current_urls = {}
        self.retry_attempts = {}
        self.using_local_video = {}
        self.tried_urls = {}
        
        # Create the video loader
        self.video_loader = VideoLoader(m3u8_links, local_videos)
        
        # Initialize players and tracking
        self._initialize_players()
    
    def _initialize_players(self):
        """Initialize media players for all tiles."""
        self.players = []
        
        for i, tile in enumerate(self.tiles):
            # Create media player
            player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
            
            # Configure player
            self.video_loader.configure_player(player)
            
            # Connect player to tile
            player.setVideoOutput(tile)
            
            # Connect signals
            player.error.connect(lambda error, p=player, idx=i: self._handle_player_error(error, p, idx))
            player.mediaStatusChanged.connect(lambda status, p=player, idx=i: self._handle_media_status_change(status, p, idx))
            
            # Add to player list
            self.players.append(player)
            
            # Initialize tracking
            self.retry_attempts[i] = 0
            self.using_local_video[i] = False
            self.tried_urls[i] = set()
    
    def assign_content_to_tiles(self):
        """
        Assign content (streams or local videos) to all tiles.
        """
        # Sort tiles by current visibility (visible tiles first)
        tile_indices = list(range(len(self.tiles)))
        random.shuffle(tile_indices)
        
        # Group 1: Tiles that need streams
        stream_indices = [i for i in tile_indices if not self.using_local_video[i]]
        
        # Group 2: Tiles that should use local videos
        local_indices = [i for i in tile_indices if self.using_local_video[i]]
        
        # Handle stream assignments first
        if self.video_loader.m3u8_links:
            # Get unique streams for this screen
            screen_name = self.video_wall.screen.name()
            max_streams = min(len(stream_indices), MAX_ACTIVE_PLAYERS, len(self.video_loader.m3u8_links))
            
            for i, idx in enumerate(stream_indices[:max_streams]):
                # Get a random stream URL that this tile hasn't tried recently
                exclude_list = self.tried_urls.get(idx, set())
                stream_url = self.video_loader.get_random_stream(exclude_list)
                
                if stream_url:
                    tile = self.tiles[idx]
                    player = self.players[idx]
                    
                    # Load and play the stream
                    if self.video_loader.load_stream(stream_url, player):
                        player.play()
                        self.current_urls[idx] = stream_url
                        self.using_local_video[idx] = False
                        tile.show_status(f"Loading stream...", duration_ms=5000)
                        print(f"Tile {idx}: Assigned stream {stream_url}")
                    else:
                        # If stream loading failed, fall back to local video
                        self._fallback_to_local_video(idx)
                else:
                    # No more streams available, use local video
                    self._fallback_to_local_video(idx)
        
        # Handle remaining tiles with local videos
        remaining_indices = local_indices + stream_indices[max_streams:]
        for idx in remaining_indices:
            self._fallback_to_local_video(idx)
    
    def _fallback_to_local_video(self, tile_index):
        """
        Fall back to a local video for a specific tile.
        
        Args:
            tile_index (int): Index of the tile
        """
        if not self.video_loader.local_videos:
            # No local videos available
            if self.tiles[tile_index].isVisible():
                self.tiles[tile_index].show_status("No media available", is_error=True)
            return
        
        # Load a random local video
        player = self.players[tile_index]
        tile = self.tiles[tile_index]
        
        video_path = self.video_loader.load_local_video(player)
        if video_path:
            player.play()
            self.current_urls[tile_index] = video_path
            self.using_local_video[tile_index] = True
            
            # Show brief status
            video_name = video_path.split('/')[-1]
            tile.show_status(f"Local: {video_name}", duration_ms=3000)
            print(f"Tile {tile_index}: Playing local video {video_name}")
        else:
            # Failed to load local video
            tile.show_status("Failed to load video", is_error=True)
    
    def pause_all_players(self):
        """Pause all media players."""
        for player in self.players:
            if player.state() == QMediaPlayer.PlayingState:
                player.pause()
    
    def resume_visible_players(self):
        """Resume playback on all visible tile media players."""
        for i, tile in enumerate(self.tiles):
            if tile.isVisible() and self.players[i].state() != QMediaPlayer.PlayingState:
                self.players[i].play()
    
    def retry_tile_stream(self, tile_index):
        """
        Retry loading a stream for a specific tile.
        
        Args:
            tile_index (int): Index of the tile to retry
        """
        # Check if we should retry
        if self.retry_attempts[tile_index] >= 3:
            # Too many retries, switch to local video
            self.retry_attempts[tile_index] = 0
            self._fallback_to_local_video(tile_index)
            return
        
        # Get a new stream URL that hasn't been tried
        exclude_list = self.tried_urls.get(tile_index, set())
        if self.current_urls.get(tile_index):
            exclude_list.add(self.current_urls[tile_index])
        
        stream_url = self.video_loader.get_random_stream(exclude_list)
        if not stream_url:
            # No streams available, use local video
            self._fallback_to_local_video(tile_index)
            return
        
        # Try the new stream
        player = self.players[tile_index]
        tile = self.tiles[tile_index]
        
        if self.video_loader.load_stream(stream_url, player):
            player.play()
            self.current_urls[tile_index] = stream_url
            self.using_local_video[tile_index] = False
            tile.show_status(f"Retrying stream...", duration_ms=3000)
            self.retry_attempts[tile_index] += 1
        else:
            # Stream loading failed
            self.tried_urls.setdefault(tile_index, set()).add(stream_url)
            self.retry_attempts[tile_index] += 1
            self.retry_tile_stream(tile_index)  # Try again with another URL
    
    def _handle_player_error(self, error, player, tile_index):
        """
        Handle media player errors.
        
        Args:
            error: The error code
            player (QMediaPlayer): The player that encountered the error
            tile_index (int): Index of the tile
        """
        if error != QMediaPlayer.NoError:
            error_message = f"Player error: {error}"
            
            # Remember failed URL
            current_url = self.current_urls.get(tile_index)
            if current_url:
                self.tried_urls.setdefault(tile_index, set()).add(current_url)
            
            # Show error briefly
            self.tiles[tile_index].show_status(error_message, is_error=True, duration_ms=2000)
            
            # Schedule retry or fallback
            QTimer.singleShot(500, lambda: self.retry_tile_stream(tile_index))
    
    def _handle_media_status_change(self, status, player, tile_index):
        """
        Handle changes in media status.
        
        Args:
            status: The media status
            player (QMediaPlayer): The player whose status changed
            tile_index (int): Index of the tile
        """
        if status == QMediaPlayer.EndOfMedia:
            # Media has ended, restart it for looping
            player.setPosition(0)
            player.play()
        
        elif status == QMediaPlayer.LoadedMedia:
            # Media loaded successfully
            if not self.using_local_video[tile_index]:
                # For streams, clear any error status
                self.tiles[tile_index].safe_hide_status()
        
        elif status == QMediaPlayer.InvalidMedia:
            # Media is invalid, try another source
            self.retry_tile_stream(tile_index)