import unittest
import main


def test_octopus_array_after_n_step(self, number_of_steps):
    initial_parser = main.LineParser(True)
    octopus_array = main.OctopusArray(initial_parser)
    for step in range(number_of_steps):
        octopus_array.run_single_step()
    step_one_parser = main.LineParser(True, number_of_steps)

    print("Test solution")
    for row in range(10):
        print(step_one_parser.get_initial_state()[row])

    print("Test Attempt")
    for row in range(10):
        line = []
        for column in range(10):
            line.append(octopus_array.get_octopus_from_array(column, row).get_energy_level())
        print(line)

    print("Flashes")
    for row in range(10):
        line = []
        for column in range(10):
            line.append(octopus_array.get_octopus_from_array(column, row).get_flash_count())
        print(line)

    print("Coords")
    for row in range(10):
        line = []
        for column in range(10):
            line.append((octopus_array.get_octopus_from_array(column, row).get_y_coordinate(), octopus_array.get_octopus_from_array(column, row).get_x_coordinate()))
        print(line)

    for row in range(10):
        for column in range(10):
            octopus_x_coordinate = octopus_array.get_octopus_from_array(column, row).get_x_coordinate()
            self.assertEqual(column, octopus_x_coordinate)

            octopus_y_coordinate = octopus_array.get_octopus_from_array(column, row).get_y_coordinate()
            self.assertEqual(row, octopus_y_coordinate)

            octopus_energy = octopus_array.get_octopus_from_array(column, row).get_energy_level()
            self.assertEqual(step_one_parser.get_initial_state()[row][column], octopus_energy)


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

    def test_octopus_array_after_one_step(self):
        test_octopus_array_after_n_step(self, 1)

    def test_octopus_array_after_two_steps(self):
        test_octopus_array_after_n_step(self, 2)



if __name__ == '__main__':
    unittest.main()
