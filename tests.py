# tests.py

import unittest
from functions.get_files_info import get_files_info


class TestFunctions(unittest.TestCase):
    def test_get_files_info_calculator_local(self):
        results = get_files_info("calculator", ".")
        print()
        print(results)
        self.assertIsNotNone(results)
        self.assertFalse(results.startswith("Error:"))

    def test_get_files_info_calculator_pkg(self):
        results = get_files_info("calculator", "pkg")
        print()
        print(results)
        self.assertIsNotNone(results)
        self.assertFalse(results.startswith("Error:"))

    def test_get_files_info_calculator_root_bin(self):
        results = get_files_info("calculator", "/bin")
        print()
        print(results)
        self.assertIsNotNone(results)
        self.assertTrue(results.startswith("Error:"))
        
    def test_get_files_info_calculator_root_parent(self):
        results = get_files_info("calculator", "../")
        print()
        print(results)
        self.assertIsNotNone(results)
        self.assertTrue(results.startswith("Error:"))

if __name__ == "__main__":
    unittest.main()