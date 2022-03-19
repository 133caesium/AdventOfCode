

class LineParser:

    def __init__(self, testing_flag=False):
        input_data = self.load_input(testing_flag)
        self.initial_state = []
        for input_line in input_data:
            output_line = []
            for number in input_line.strip():
                output_line.append(int(number))
            self.initial_state.append(output_line)

    def get_initial_state(self):
        return self.initial_state

    def load_input(self, testing_flag):
        input_path = "./input.txt"
        if testing_flag:
            input_path = "./sample_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines

class BioluminescentOctopus:

    def __init__(self, x_coordinate: int, y_coordinate: int, intial_value: int):
        self.__energy_level = intial_value
        self.__steps_counted = 0
        self.__flashed_this_step = False
        self.__flash_counts = 0
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate

    def increment_step(self):
        self.__steps_counted += 1

    def flash(self):
        pass

    def get_energy_level(self):
        return self.__energy_level

    def get_x_coordinate(self):
        return self.__x_coordinate

    def get_y_coordinate(self):
        return self.__y_coordinate

class OctopusArray:

    def __init__(self, parser: LineParser):
        self.__octopus_array = self.generate_octopus_array(parser.get_initial_state())

    def get_octopus_array(self):
        return self.__octopus_array

    def get_octopus_from_array(self, x_coordinate: int, y_coordinate: int):
        return self.__octopus_array[y_coordinate][x_coordinate]


    def generate_octopus_array(self, raw_values):
        octopus_array = []
        y_coordinate = 0
        for row in raw_values:
            octopus_row = []
            x_coordinate = 0
            for octopus_inital_state in row:
                octopus_row.append(BioluminescentOctopus(x_coordinate,y_coordinate,octopus_inital_state))
                x_coordinate += 1
            octopus_array.append(octopus_row)
            y_coordinate += 1
        return octopus_array





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("nothing to see here")