class Fish:
    def __init__(self, birthday, state=9):
        self.birthday = birthday
        self.internal_state = state
        self.create_fish_today = False

    def day_passes(self):
        self.internal_state -= 1
        if self.internal_state == 0:
            self.create_fish_today = True
        else:
            self.create_fish_today = False
        if self.internal_state<0:
            self.internal_state = 6

class Sea:
    def __init__(self):
        self.day = 0
        self.fish = []

    def create_fish(self, parser):
        for fish_state in parser.get_initial_state():
            new_fish = Fish(fish_state-8, fish_state)
            self.fish.append(new_fish)

    def time_passes(self):
        self.spawn_days_new_fish()
        self.day += 1
        for fish in self.fish:
            fish.day_passes()


    def spawn_days_new_fish(self):
        for fish in self.fish:
            if fish.create_fish_today:
                self.fish.append(Fish(self.day))

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



def printStates():
    states = []
    for fish in sea.fish:
        states.append(fish.internal_state)
    print("After {} days: {}".format(sea.day,states))

if __name__ == '__main__':
    sea = Sea()
    parser = LineParser()
    sea.create_fish(parser)
    printStates()
    while sea.day < 256:
        sea.time_passes()
        print("day: {}, fish: {}".format(sea.day, len(sea.fish)))
        # printStates()






