import unittest
import solution

input = open("simple_input.txt").read().strip()
input2 = open("simple_input2.txt").read().strip()
input3 = open("simple_input3.txt").read().strip()
race_track = open("simple_race_track.txt").read().strip()

class Quest07Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual("BDCA", solution.part1(input))

    def test_part2(self):
        self.assertEqual("DCBA", solution.part2(input2, race_track))

    def test_part3(self):
        self.assertEqual(0, solution.part3(input3, race_track))

if __name__ == "__main__":
    unittest.main()




















