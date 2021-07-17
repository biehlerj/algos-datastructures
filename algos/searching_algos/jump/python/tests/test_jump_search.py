from jump_search.jump_search import jump_search
import unittest


class TestJumpSearch(unittest.TestCase):
    test_array = [2, 3, 4, 10, 40]
    
    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Functionality .....')
        print('.......  For Jump Search  .......')
        print('.................................\n\n')

    def test_good_search(self):
        target = 10
        result = jump_search(self.test_array, len(self.test_array), target)
        self.assertEquals(result, 3)

    def test_bad_search(self):
        target = 69
        result = jump_search(self.test_array, len(self.test_array), target)
        self.assertEquals(result, -1)


if __name__ == '__main__':
    """
    Main Tests
    """
    unittest.main
