import re

class LineParser:

    def __init__(self, testing_flag=False, offset=0, separation=12, array_size=10):
        input_data = self.load_input(testing_flag)
        self.initial_state = []
        cave_lines = []
        for line in input_data:
            if (line=='\n'):
                self.initial_state.append(cave_lines)
                cave_lines = []
            else:
                cave_lines.append(line.strip())
        self.initial_state.append(cave_lines)

    def get_initial_state(self):
        return self.initial_state

    def load_input(self, testing_flag):
        input_path = "./input.txt"
        if testing_flag:
            input_path = "./sample_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines

class Cave:
    def __init__(self, id):
        self.__id = id
        self.__big_cave = id.isupper()
        self.__connected_caves = set()
        self.__times_visited = 0

    def add_connected_cave(self, cave_id):
        self.__connected_caves.add(cave_id)

    def add_visit(self):
        self.__times_visited += 1

    def get_id(self):
        return self.__id

    def is_big(self):
        return self.__big_cave

    def get_visits(self):
        return self.__times_visited

    def get_connected_caves(self):
        return self.__connected_caves

    def __eq__(self, other):
        if isinstance(other, Cave):
            return self.__hash__() == other.__hash__()
        else:
            return False

    def __hash__(self):
        return hash(self.__id)

    def __repr__(self):
        return f'Cave-{self.__id}'

def get_cave_set(cave_text):
    caves = {}
    for connection in cave_text:
        cave1, cave2 = connection.split('-')
        if cave1 not in caves:
            new_cave1 = Cave(cave1)
            caves[cave1] = new_cave1
        if cave2 not in caves:
            new_cave2 = Cave(cave2)
            caves[cave2] = new_cave2
        caves[cave1].add_connected_cave(cave2)
        caves[cave2].add_connected_cave(cave1)

    return caves

def initalise_caves():
    bulk_cave_text = LineParser(True)
    individual_cave_text = bulk_cave_text.initial_state[0][1:]
    caves = get_cave_set(individual_cave_text)
    print(caves)
    return caves

if __name__ == '__main__':
    caves = initalise_caves()
    for cave in caves:
        print(f'This cave is called {caves[cave].get_id()} and it`s big status is {caves[cave].is_big()} and it connects to {caves[cave].get_connected_caves()}')
