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

    def test_octopus_array_creation(self):
        sample_parser = main.LineParser(True)
        octopus_array = main.OctopusArray(sample_parser)
        for row in range(10):
            for column in range(10):
                octopus_x_coordinate = octopus_array.get_octopus_from_array(column, row).get_x_coordinate()
                self.assertEqual(column, octopus_x_coordinate)

                octopus_y_coordinate = octopus_array.get_octopus_from_array(column, row).get_y_coordinate()
                self.assertEqual(row, octopus_y_coordinate)

                octopus_energy = octopus_array.get_octopus_from_array(column, row).get_energy_level()
                self.assertEqual(sample_parser.get_initial_state()[row][column], octopus_energy)



if __name__ == '__main__':
    unittest.main()
