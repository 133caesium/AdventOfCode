import unittest
from day5 import LineCoordinates
from day5 import LineParser
from day5 import HydrothermalMap

class MyTestCase(unittest.TestCase):

    def test_line_coordinates(self):
        test_line = LineCoordinates("0,9 -> 5,9")
        self.assertEqual(0, test_line.get_x1())
        self.assertEqual(9, test_line.get_y1())
        self.assertEqual(5, test_line.get_x2())
        self.assertEqual(9, test_line.get_y2())

    def test_horizontal_line_coordinates(self):
        test_line = LineCoordinates("0,9 -> 5,9")
        self.assertEqual(True, test_line.get_horizontal())
        self.assertEqual(False, test_line.get_vertical())

    def test_vertical_line(self):
        test_line = LineCoordinates("7,0 -> 7,4")
        self.assertEqual(False, test_line.get_horizontal())
        self.assertEqual(True, test_line.get_vertical())

    def test_create_parser(self):
        parser = LineParser(True)

    def test_parser_max(self):
        parser = LineParser(True)
        self.assertEqual(9,parser.get_max_x())
        self.assertEqual(9, parser.get_max_y())

    def test_parser_line_one(self):
        parser = LineParser(True)
        test_line = parser.get_lines()[0]
        self.assertEqual(0, test_line.get_x1())
        self.assertEqual(9, test_line.get_y1())
        self.assertEqual(5, test_line.get_x2())
        self.assertEqual(9, test_line.get_y2())

    def test_hydrothermal(self):
        parser = LineParser(True)
        hydrothermal_map = HydrothermalMap(parser)

    def test_hydrothermal(self):
        parser = LineParser(True)
        hydrothermal_map = HydrothermalMap(parser)
        hydrothermal_map.plot_all_lines()









if __name__ == '__main__':
    unittest.main()
