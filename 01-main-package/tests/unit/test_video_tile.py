"""
Unit tests for VideoTile class.
"""
import unittest
from PyQt5.QtWidgets import QApplication
from videowall.ui.video_tile import VideoTile

class TestVideoTile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create QApplication instance for tests
        cls.app = QApplication([])
        
    def setUp(self):
        # Create a tile for each test
        self.tile = VideoTile(1)
        
    def test_initialization(self):
        """Test that the VideoTile initializes correctly."""
        self.assertEqual(self.tile.tile_id, 1)
        self.assertEqual(self.tile.objectName(), "Tile_1")
        self.assertTrue(self.tile.status_label.isVisible())
        
    def test_show_status(self):
        """Test status display functionality."""
        self.tile.show_status("Test Status")
        self.assertTrue(self.tile.status_label.isVisible())
        self.assertEqual(self.tile.status_label.text(), "Test Status")
        
    def test_error_status(self):
        """Test error status display."""
        self.tile.show_status("Error", is_error=True)
        self.assertIn("rgba(150, 0, 0", self.tile.status_label.styleSheet())
        
    def tearDown(self):
        # Clean up
        self.tile.deleteLater()

if __name__ == "__main__":
    unittest.main()