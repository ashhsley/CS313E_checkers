import unittest
from Racko_Project import TreeRack, heap_invariant


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.rack1 = TreeRack([1, 2, 3, 4, 5, 6, 7, 8])
        # An array sorted in ascending order should naturally have heap property

        self.rack2 = TreeRack([10, 5, 6, 3, 21, 6, 8, 3, 5, 1, 35])
        # Since the first element is greater than the second, we should expect the heap property break here

        self.rack3 = TreeRack([3, 5, 6, 10, 7, 20, 13, 9, 5, 15, 21, 22, 24, 14, 19])
        # Here the 10 occupies position 3 and its left child (position 2*3+1 = 7) is 9 so the property is violated
        # But after the heap property is maintained if we only look at the right subtree (starting at index 2)

        self.rack4 = TreeRack([3, 5, 10, 7, 9, 14, 15])
        # Even though the array is not sorted, the heap invariance can be preserved !!!

    def test_whole_1(self):
        self.assertTrue(heap_invariant(self.rack1, 0))

    def test_whole_2(self):
        self.assertFalse(heap_invariant(self.rack2, 0))

    def test_middle(self):
        self.assertFalse(heap_invariant(self.rack3, 0))

    def test_subtree(self):
        self.assertTrue(heap_invariant(self.rack3, 2))

    def test_order(self):
        self.assertTrue(heap_invariant(self.rack4, 0))


if __name__ == '__main__':
    unittest.main()
