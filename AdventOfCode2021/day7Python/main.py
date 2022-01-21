import statistics


class LineParser:
    def __init__(self, testing_flag=False):
        input_data = self.load_input(testing_flag)
        input_strings=input_data[0].split(",")
        self.initial_state = []
        for number in input_strings:
            self.initial_state.append(int(number))

    def get_initial_state(self):
        return self.initial_state

    def load_input(self, testing_flag):
        input_lines = []
        input_path = "./input.txt"
        if testing_flag:
            input_path = "./test_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines


def triangle(n):
    return (n*(n+1))/2

def fuel_calculator(crabs, position):
    fuel = 0
    for crab in crabs:
        # fuel = fuel + abs(crab - position)
        fuel += triangle(abs(crab-position))
    return fuel

def day7_part1_solver():
    parser = LineParser()
    crabs = parser.get_initial_state()

    median_crab = statistics.median(crabs)

    print(median_crab)

    print(fuel_calculator(crabs, median_crab))

    print(min(crabs))

def day7_part2_solver():
    parser = LineParser()
    crabs = parser.get_initial_state()
    first_crab = min(crabs)
    last_crab = max(crabs)
    current_position = first_crab
    min_fuel = fuel_calculator(crabs, current_position)
    best_position = current_position
    while current_position < last_crab:
        current_position += 1
        new_fuel = fuel_calculator(crabs, current_position)
        if new_fuel < min_fuel:
            min_fuel = new_fuel
            best_position = current_position
    print("Cheapeast unifying position is: {} costing: {}".format(best_position, min_fuel))


if __name__ == '__main__':
    day7_part1_solver()
    day7_part2_solver()