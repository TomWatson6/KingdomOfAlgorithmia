import unittest
import solution

input = open("simple_input.txt").read().strip()
input2 = open("simple_input2.txt").read().strip()
input3 = open("simple_input3.txt").read().strip()
input4 = open("simple_input4.txt").read().strip()

class Quest07Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(7, solution.part1(input))

    def test_part2(self):
        self.assertEqual(32, solution.part2(input2))

    def test_part3(self):
        self.assertEqual(5, solution.part3(input3))

    def test_part3_ex2(self):
        self.assertEqual(46, solution.part3(input4))

if __name__ == "__main__":
    unittest.main()




















