import numpy as np
from datetime import datetime

class LineParser:

    def __init__(self, testing_flag=False, offset=0, separation=12, array_size=10):
        input_data = self.load_input(testing_flag)
        height = len(input_data)
        width = len(input_data[0])
        cavern_map = np.zeros((height,width-1))
        for y in range(height):
            for x in range(width-1):
                cavern_map[y, x] = int(input_data[y][x])

        self.initial_state = cavern_map

    def get_initial_state(self):
        return self.initial_state

    def load_input(self, testing_flag):
        input_path = "./input.txt"
        if testing_flag:
            input_path = "./sample_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines


def get_possible_moves(x, y, cave_map):
    y_max, x_max = cave_map.shape
    possible_moves = {}
    possible_moves['up'] = (x, y+1)
    possible_moves['right'] = (x+1, y)
    possible_moves['down'] = (x, y-1)
    possible_moves['left'] = (x-1, y)
    moves = {}
    for move in possible_moves:
        if (possible_moves[move][0] in range(0, x_max)) and (possible_moves[move][1] in range(0, y_max)):
                moves[move] = possible_moves[move]
    return moves


class Path:
    path_id = 0

    def __init__(self, cave_map, path_list=[(0,0)]):
        self.__id = Path.path_id
        Path.path_id += 1
        self.__cave_map = cave_map
        self.__path_list = path_list

    def add_move_to_path(self, move):
        current_location = self.__path_list[-1]
        possible_moves = get_possible_moves(current_location[0], current_location[1], self.__cave_map):
        if move.value in possible_moves.values():
            self.__path_list.append(possible_moves[move])


    def get_id(self):
        return self.__id

    def get_visted_small_twice(self):
        return self.__visited_a_small_cave_twice

    def is_complete(self):
        return self.__path_list[-1] == 'end'

    def get_last_cave_id(self):
        return self.__path_list[-1]

    def get_path_list(self):
        return self.__path_list

    def get_next_caves(self):
        next_caves = []
        possible_caves = self.__cave_network_set[self.__path_list[-1]].get_connected_caves()
        for cave in possible_caves:
            if cave != 'start':
                if self.__cave_network_set[cave].is_big() or self.__cave_network_set[cave].get_visits() == 0 or \
                        (self.__cave_network_set[cave].get_visits() == 1 and not self.__visited_a_small_cave_twice):
                    next_caves.append(cave)
        return next_caves

    def get_cave_network(self):
        return self.__cave_network_set

    def __eq__(self, other):
        if isinstance(other, Path):
            return self.__hash__() == other.__hash__()
        else:
            return False

    def __hash__(self):
        return hash(''.join(self.__path_list))

    def __repr__(self):
        return f'[Path ID: {self.__id}, Path: {"-".join(self.__path_list)}]'





if __name__ == '__main__':
    verbose = False
    use_sample_input = False
    total_steps = 40

    cavern_map = LineParser(True, True).get_initial_state()

    starting_location = (0,0)
    ending_location = (cavern_map.shape[0]-1, cavern_map.shape[1]-1)

    # for move in get_possible_moves()

    print(get_possible_moves(starting_location[0], starting_location[1], cavern_map))