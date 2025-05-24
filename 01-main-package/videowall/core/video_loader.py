"""
Video loading and management functionality.
"""
import os
import random
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

from videowall.utils.file_utils import get_video_files_recursively, get_all_m3u8_links
from videowall.config.settings import VIDEO_BUFFER_SIZE, LOW_LATENCY_MODE, HARDWARE_DECODE_PRIORITY

class VideoLoader:
    """
    Handles loading of videos from various sources and prepares them for display.
    """
    
    def __init__(self, m3u8_links=None, local_videos=None):
        """
        Initialize the video loader.
        
        Args:
            m3u8_links (list, optional): List of M3U8 stream URLs
            local_videos (list, optional): List of local video file paths
        """
        self.m3u8_links = m3u8_links or []
        self.local_videos = local_videos or []
        self.recently_used_videos = []
        self.failed_streams = set()
        
    def load_stream(self, url, player):
        """
        Load an M3U8 stream into a media player.
        
        Args:
            url (str): Stream URL
            player (QMediaPlayer): Media player to load the stream into
            
        Returns:
            bool: True if loading initiated successfully, False otherwise
        """
        try:
            if not url or not player:
                return False
                
            # Create a QMediaContent object with the stream URL
            media_content = QMediaContent(QUrl(url))
            
            # Configure player settings for streaming
            player.setBufferSize(VIDEO_BUFFER_SIZE)
            
            # Set playback rate options for streaming
            if LOW_LATENCY_MODE:
                player.setPlaybackRate(1.01)  # Slightly faster to catch up
            
            # Set media and initiate playback
            player.setMedia(media_content)
            
            return True
        except Exception as e:
            print(f"Error loading stream {url}: {e}")
            self.failed_streams.add(url)
            return False
            
    def load_local_video(self, player):
        """
        Load a random local video into a media player, avoiding recently used videos.
        
        Args:
            player (QMediaPlayer): Media player to load the video into
            
        Returns:
            str: Path to the loaded video file, or None if loading failed
        """
        if not self.local_videos:
            return None
            
        # Get available videos that weren't recently used
        available_videos = [v for v in self.local_videos if v not in self.recently_used_videos]
        
        # If all videos have been recently used, reset and use all videos
        if not available_videos:
            self.recently_used_videos = []
            available_videos = self.local_videos
            
        if not available_videos:
            return None
            
        # Select a random video from available options
        selected_video = random.choice(available_videos)
        
        try:
            # Create QMediaContent with local file path
            file_url = QUrl.fromLocalFile(selected_video)
            media_content = QMediaContent(file_url)
            
            # Set media and playback options
            player.setMedia(media_content)
            
            # Add to recently used and keep list at reasonable size
            self.recently_used_videos.append(selected_video)
            if len(self.recently_used_videos) > min(len(self.local_videos) // 2, 20):
                self.recently_used_videos.pop(0)  # Remove oldest entry
                
            return selected_video
        except Exception as e:
            print(f"Error loading local video {selected_video}: {e}")
            return None
    
    def configure_player(self, player):
        """
        Configure a QMediaPlayer with optimal settings.
        
        Args:
            player (QMediaPlayer): Media player to configure
        """
        # Set hardware decoding preference
        if HARDWARE_DECODE_PRIORITY:
            player.setProperty("videoCodecOptions", {
                "hwaccel": "videotoolbox",  # For macOS
                "hwaccel_device": "auto",
                "hwaccel_output_format": "nv12",
            })
            
        # Set audio settings (muted)
        player.setMuted(True)
        player.setVolume(0)
        
        # Set buffer size for smoother playback
        player.setBufferSize(VIDEO_BUFFER_SIZE)
        
        # Set network options for streaming
        player.setProperty("network-caching", 1500)  # 1.5 seconds network cache
        
    def get_random_stream(self, exclude_list=None):
        """
        Get a random stream URL, avoiding those in the exclude list.
        
        Args:
            exclude_list (list, optional): List of URLs to exclude
            
        Returns:
            str: Stream URL, or None if no viable streams available
        """
        if not self.m3u8_links:
            return None
            
        exclude_set = set(exclude_list or [])
        exclude_set.update(self.failed_streams)
        
        # Filter available streams
        available_streams = [url for url in self.m3u8_links if url not in exclude_set]
        
        if not available_streams:
            # If all streams are excluded, reset failed streams and try again
            if self.failed_streams:
                self.failed_streams.clear()
                return self.get_random_stream(exclude_list)
            # If still no streams, return None
            return None
            
        return random.choice(available_streams)