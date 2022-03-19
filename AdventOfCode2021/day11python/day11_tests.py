import unittest
import main


class Test_Day_11_Code(unittest.TestCase):
    def test_line_parser(self):
        sample_parser = main.LineParser(True)
        sum_of_initial_values = 0
        for row in sample_parser.get_initial_state():
            for value in row:
                sum_of_initial_values += value
        self.assertEqual(446, sum_of_initial_values)


if __name__ == '__main__':
    unittest.main()
