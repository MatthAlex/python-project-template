"""Sample test file"""

import unittest
from unittest.mock import MagicMock

from src.main import main


class TestMainEntryPoint(unittest.TestCase):
    """Test script entry point."""

    def setUp(self) -> None:
        # This is not yet needed but illustrates how we can prime common functionality
        self.mock_logger = MagicMock()

    def test_main(self) -> None:
        """Test that the main function prints the correct string."""
        # arrange
        expected_value = "Hello World!"

        # act
        tested_value = main()

        # assert
        self.assertEqual(expected_value, tested_value)
