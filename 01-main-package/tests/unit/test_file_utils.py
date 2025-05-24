"""
Unit tests for file utility functions.
"""
import unittest
import os
import tempfile
from videowall.utils.file_utils import get_all_m3u8_links, get_video_files_recursively

class TestFileUtils(unittest.TestCase):
    def setUp(self):
        """Set up temporary files for testing."""
        # Create a temporary directory
        self.temp_dir = tempfile.TemporaryDirectory()
        
        # Create a temporary M3U8 file
        self.m3u8_file = os.path.join(self.temp_dir.name, "test.m3u8")
        with open(self.m3u8_file, "w") as f:
            f.write("# Test M3U8 file\n")
            f.write("https://example.com/stream1.m3u8\n")
            f.write("https://example.com/stream2.m3u8\n")
            f.write("example.com/stream3.m3u8\n")  # No protocol
        
        # Create some test video files
        self.video_dir = os.path.join(self.temp_dir.name, "videos")
        os.mkdir(self.video_dir)
        
        # Create valid video files
        open(os.path.join(self.video_dir, "video1.mp4"), "w").close()
        open(os.path.join(self.video_dir, "video2.mkv"), "w").close()
        
        # Create subdirectory with videos
        os.mkdir(os.path.join(self.video_dir, "subdir"))
        open(os.path.join(self.video_dir, "subdir", "video3.avi"), "w").close()
        
        # Create hidden files that should be ignored
        open(os.path.join(self.video_dir, ".hidden.mp4"), "w").close()
        open(os.path.join(self.video_dir, "._metadata.mp4"), "w").close()
        
    def test_get_all_m3u8_links(self):
        """Test parsing M3U8 files."""
        links = get_all_m3u8_links(self.m3u8_file)
        
        # Should find 3 links, with the protocol-less one getting https:// added
        self.assertEqual(len(links), 3)
        self.assertIn("https://example.com/stream1.m3u8", links)
        self.assertIn("https://example.com/stream2.m3u8", links)
        self.assertIn("https://example.com/stream3.m3u8", links)
        
    def test_get_all_m3u8_links_nonexistent_file(self):
        """Test handling of nonexistent files."""
        links = get_all_m3u8_links("/nonexistent/file.m3u8")
        self.assertEqual(links, [])
        
    def test_get_video_files_recursively(self):
        """Test recursive video file scanning."""
        videos = get_video_files_recursively(self.video_dir)
        
        # Should find 3 videos (2 in main directory, 1 in subdirectory)
        self.assertEqual(len(videos), 3)
        
        # Check that we got the right files
        filenames = [os.path.basename(v) for v in videos]
        self.assertIn("video1.mp4", filenames)
        self.assertIn("video2.mkv", filenames)
        self.assertIn("video3.avi", filenames)
        
        # Make sure hidden files are not included
        self.assertNotIn(".hidden.mp4", filenames)
        self.assertNotIn("._metadata.mp4", filenames)
        
    def tearDown(self):
        """Clean up temporary files."""
        self.temp_dir.cleanup()

if __name__ == "__main__":
    unittest.main()