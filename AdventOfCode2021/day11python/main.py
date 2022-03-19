

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




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("nothing to see here")