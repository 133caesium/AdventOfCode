class Sea:
    def __init__(self):
        self.day = 0
        self.fish = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def create_fish(self, parser):
        for fish_state in parser.get_initial_state():
            self.fish[fish_state] += 1

    def time_passes(self):
        self.spawn_days_new_fish()
        self.day += 1
        index = 0
        self.fish[7] += self.fish[0]
        self.fish[0] = 0
        while index < 9:
            self.fish[index] += self.fish[index+1]
            self.fish[index+1] = 0
            index += 1

    def spawn_days_new_fish(self):
        sea.fish[9] = sea.fish[0]

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


if __name__ == '__main__':
    sea = Sea()
    parser = LineParser()
    sea.create_fish(parser)
    while sea.day < 257:
        num_fish = 0
        for fish in sea.fish:
            num_fish += fish
        print("day: {}, fish: {}, sea: {}".format(sea.day, num_fish, sea.fish))
        sea.time_passes()
        # printStates()






