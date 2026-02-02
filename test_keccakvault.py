# test_keccakvault.py
"""
Tests for KeccakVault module.
"""

import unittest
from keccakvault import KeccakVault

class TestKeccakVault(unittest.TestCase):
    """Test cases for KeccakVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KeccakVault()
        self.assertIsInstance(instance, KeccakVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KeccakVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
