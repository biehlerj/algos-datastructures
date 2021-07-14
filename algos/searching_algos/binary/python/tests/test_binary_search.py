from binary_search.binary_search import binary_search
import unittest


class TestBinarySearch(unittest.TestCase):

    test_array = [2, 3, 4, 10, 40]
    x = 10

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Functionality .....')
        print('......  For Binary Search  ......')
        print('.................................\n\n')

    def test_good_search(self):
        result = binary_search(self.test_array, len(self.test_array), self.x)
        self.assertEquals(result, 3)

    def test_bad_search(self):
        result = binary_search(self.test_array, len(self.test_array), 25)
        self.assertEquals(result, -1)


if __name__ == '__main__':
    """
    Main Tests
    """
    unittest.main
