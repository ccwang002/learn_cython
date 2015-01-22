import unittest

from iteration import I

class TestIteration(unittest.TestCase):
    def setUp(self):
        self.i = I()

    def test_iteration(self):
        self.assertEqual(len(list(self.i)), 100)

    def test_iteration_summation(self):
        self.assertEqual(sum(self.i), 4950)
