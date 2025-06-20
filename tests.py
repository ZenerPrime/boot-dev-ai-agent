# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


# class TestFunctions(unittest.TestCase):
#     def test_get_files_info_calculator_local(self):
#         results = get_files_info("calculator", ".")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertFalse(results.startswith("Error:"))

#     def test_get_files_info_calculator_pkg(self):
#         results = get_files_info("calculator", "pkg")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertFalse(results.startswith("Error:"))

#     def test_get_files_info_calculator_root_bin(self):
#         results = get_files_info("calculator", "/bin")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertTrue(results.startswith("Error:"))
        
#     def test_get_files_info_calculator_root_parent(self):
#         results = get_files_info("calculator", "../")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertTrue(results.startswith("Error:"))
            
#     def test_get_file_content_calculator_lorem(self):
#         results = get_file_content("calculator", "lorem.txt")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertTrue(results.endswith('[...File "lorem.txt" truncated at 10000 characters]'))

#     def test_get_file_content_calculator_main(self):
#         results = get_file_content("calculator", "main.py")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertFalse(results.startswith("Error:"))

#     def test_get_file_content_calculator_pkg_calculator(self):
#         results = get_file_content("calculator", "pkg/calculator.py")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertFalse(results.startswith("Error:"))

#     def test_get_file_content_root_bin_cat(self):
#         results = get_file_content("calculator", "/bin/cat")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertTrue(results.startswith("Error:"))
    
#     def test_write_file_calculator_lorem(self):
#         results = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertTrue("Successfully wrote to " in results)

#     def test_write_file_calculator_pkg_morelorem(self):
#         results = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertTrue("Successfully wrote to " in results)

#     def test_write_file_calculator_root_tcleamp_temp(self):
#         results = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertTrue(results.startswith("Error:"))

#     def test_run_python_file_calculator_main(self):
#         results = run_python_file("calculator", "main.py")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertFalse(results.startswith("Error:"))

#     def test_run_python_file_calculator_tests(self):
#         results = run_python_file("calculator", "tests.py")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertFalse(results.startswith("Error:"))

#     def test_run_python_file_main(self):
#         results = run_python_file("calculator", "../main.py")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertTrue(results.startswith("Error:"))

#     def test_run_python_file_calculator_nonexistent(self):
#         results = run_python_file("calculator", "nonexistent.py")
#         print()
#         print(results)
#         self.assertIsNotNone(results)
#         self.assertTrue(results.startswith("Error:"))

# if __name__ == "__main__":
#     unittest.main()

print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))