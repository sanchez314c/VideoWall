"""
Main application entry point.
"""
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from videowall.core.video_wall import VideoWall
from videowall.ui.dialogs import LocalVideoDialog
from videowall.utils.file_utils import get_all_m3u8_links, get_video_files_recursively
from videowall.config.settings import ICON_PATH

def main():
    """
    Initialize and run the VideoWall application.
    """
    app = QApplication(sys.argv)
    
    # Set application icon
    if os.path.exists(ICON_PATH):
        app.setWindowIcon(QIcon(ICON_PATH))
    
    # Get M3U8 links
    m3u8_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
                             "video-wall-m3u8-hosts.m3u8")
    m3u8_links = get_all_m3u8_links(m3u8_path) if os.path.exists(m3u8_path) else []
    
    # Show configuration dialog
    dialog = LocalVideoDialog()
    result = dialog.exec_()
    
    if result == 0:  # User canceled
        return 0
        
    config = dialog.get_results()
    
    # Get local videos if enabled
    local_videos = []
    if config["use_local_videos"] and config["folder_path"]:
        local_videos = get_video_files_recursively(config["folder_path"])
    
    # Create video wall for each screen
    screens = app.screens()
    video_walls = []
    
    for screen in screens:
        wall = VideoWall(app, m3u8_links, local_videos, screen)
        video_walls.append(wall)
    
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())