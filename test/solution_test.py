import unittest
from solution import solve
from random import shuffle, choices


class TestRiddle(unittest.TestCase):

    def stress_test(self, count, generator_func):
        for x in range(count):
            picked_nums = generator_func()
            shuffle(picked_nums)
            prisoner = solve(picked_nums)
            self.assertNotEqual(prisoner, None)

    def test_repeat(self):
        self.stress_test(1000, lambda: choices(range(1, 10), k=10))
        self.stress_test(1000, lambda: choices(range(1, 7), k=7))
        self.stress_test(100, lambda: choices(range(1, 3), k=3))
        self.stress_test(10, lambda: choices(range(1, 2), k=2))


if __name__ == '__main__':
    unittest.main()
