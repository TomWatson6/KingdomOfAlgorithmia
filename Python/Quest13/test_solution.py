import unittest
import solution

input = open("simple_input.txt").read().strip()
input2 = open("simple_input2.txt").read().strip()
input3 = open("simple_input3.txt").read().strip()

class Quest13Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(28, solution.part1(input))

    def test_part2(self):
        self.assertEqual(28, solution.part2(input2))

    def test_part3(self):
        self.assertEqual(14, solution.part3(input3))

if __name__ == "__main__":
    unittest.main()




















