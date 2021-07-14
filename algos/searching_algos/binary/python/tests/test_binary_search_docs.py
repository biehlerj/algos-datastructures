from binary_search.binary_search import binary_search
import inspect
import pep8
import unittest


class TestBinarySearchDocs(unittest.TestCase):

    all_funcs = inspect.getmembers(binary_search, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('......  For Binary Search  ......')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        actual = binary_search.__doc__
        self.assertIsNotNone(actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in binary_search"""
        all_functions = TestBinarySearchDocs.all_funcs
        for function in all_functions:
            self.assertIsNotNone(function[1].__doc__)

    def test_pep8(self):
        """... ensure binary_search.py conforms to PEP8 Style"""
        pep8_style = pep8.StyleGuide(quiet=True)
        errors = pep8_style.check_files(['binary_search/binary_search.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)


if __name__ == '__main__':
    """
    Main Tests
    """
    unittest.main
