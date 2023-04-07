import unittest

import main


class MyTestCase(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual([1, 2, 3, 4], main.remove_duplicates([1, 2, 3, 4]))

    def test_merge_list(self):
        self.assertEqual([], main.intersect([1, 2, 3, 4, 5, 6], []))

    def test_merge_lists(self):
        list1 = [1, 2, 6, 8, 9]
        list2 = [1, 2, 4, 5, 8]
        list3 = [1, 1, 2, 2, 4, 5, 6, 8, 8, 9]
        self.assertEqual(list3, main.merge(list1, list2))


if __name__ == '__main__':
    unittest.main()
