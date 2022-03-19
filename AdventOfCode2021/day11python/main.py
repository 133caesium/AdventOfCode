

class LineParser:

    def __init__(self, testing_flag=False, offset=0, separation=12, array_size=10):
        input_data = self.load_input(testing_flag)
        self.initial_state = []
        for input_line_index in range(offset*separation, offset*separation+array_size):
            input_line = input_data[input_line_index]
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
        self.increment_energy()


    def flash(self):
        flash_happened = False
        if self.__energy_level > 9 and not self.__flashed_this_step:
            self.__flash_counts += 1
            self.__flashed_this_step = True
            flash_happened = True
        return flash_happened

    def flash_reset(self):
        if self.__flashed_this_step:
            self.__energy_level = 0
            self.__flashed_this_step = False

    def increment_energy(self):
        self.__energy_level += 1

    def get_energy_level(self):
        return self.__energy_level

    def get_x_coordinate(self):
        return self.__x_coordinate

    def get_y_coordinate(self):
        return self.__y_coordinate

    def get_flash_count(self):
        return self.__flash_counts

class OctopusArray:
    def __init__(self, parser: LineParser):
        self.__octopus_array = self.generate_octopus_array(parser.get_initial_state())

    def run_single_step(self):
        self.increment_step()
        self.flash_step()
        self.finish_step()

    def increment_step(self):
        for row in self.__octopus_array:
            for octopus in row:
                octopus.increment_step()

    def flash_step(self):
        flashing = True
        while flashing:
            flashing = False
            for row in self.__octopus_array:
                for octopus in row:
                    if octopus.flash():
                        # print("flash detected")
                        self.flash_neighbours(octopus.get_x_coordinate(), octopus.get_y_coordinate())
                        flashing = True


    def finish_step(self):
        for row in self.__octopus_array:
            for octopus in row:
                octopus.flash_reset()

    def flash_neighbours(self, flash_row, flash_column):
        for row in range(flash_row-1, flash_row+2):
            if row in range(10):
                for column in range(flash_column-1, flash_column+2):
                    if column in range(10):
                        self.get_octopus_from_array(column, row).increment_energy()
                        # print("adding 1 energy to octopus at x={}, y={}".format(column,row))

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