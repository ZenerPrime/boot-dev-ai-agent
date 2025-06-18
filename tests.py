# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


class TestFunctions(unittest.TestCase):
    # def test_get_files_info_calculator_local(self):
    #     results = get_files_info("calculator", ".")
    #     print()
    #     print(results)
    #     self.assertIsNotNone(results)
    #     self.assertFalse(results.startswith("Error:"))

    # def test_get_files_info_calculator_pkg(self):
    #     results = get_files_info("calculator", "pkg")
    #     print()
    #     print(results)
    #     self.assertIsNotNone(results)
    #     self.assertFalse(results.startswith("Error:"))

    # def test_get_files_info_calculator_root_bin(self):
    #     results = get_files_info("calculator", "/bin")
    #     print()
    #     print(results)
    #     self.assertIsNotNone(results)
    #     self.assertTrue(results.startswith("Error:"))
        
    # def test_get_files_info_calculator_root_parent(self):
    #     results = get_files_info("calculator", "../")
    #     print()
    #     print(results)
    #     self.assertIsNotNone(results)
    #     self.assertTrue(results.startswith("Error:"))
            
    # def test_get_file_content_calculator_lorem(self):
    #     results = get_file_content("calculator", "lorem.txt")
    #     print()
    #     print(results)
    #     self.assertIsNotNone(results)
    #     self.assertTrue(results.endswith('[...File "lorem.txt" truncated at 10000 characters]'))

    def test_get_file_content_calculator_main(self):
        results = get_file_content("calculator", "main.py")
        print()
        print(results)
        self.assertIsNotNone(results)
        self.assertFalse(results.startswith("Error:"))

    def test_get_file_content_calculator_pkg_calculator(self):
        results = get_file_content("calculator", "pkg/calculator.py")
        print()
        print(results)
        self.assertIsNotNone(results)
        self.assertFalse(results.startswith("Error:"))

    def test_get_file_content_root_bin_cat(self):
        results = get_file_content("calculator", "/bin/cat")
        print()
        print(results)
        self.assertIsNotNone(results)
        self.assertTrue(results.startswith("Error:"))

if __name__ == "__main__":
    unittest.main()