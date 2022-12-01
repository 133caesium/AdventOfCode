import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

class LineParser:

    def __init__(self, testing_flag=False):
        input_data = self.load_input(testing_flag)
        height = len(input_data)
        width = len(input_data[0])

        cavern_map = np.zeros((height, width - 1))
        for y in range(height):
            for x in range(width - 1):
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


class CaveLocation:

    def __init__(self, x, y, width, height, risk):
        self.x = x
        self.y = y
        self.risk = risk
        self.min_cost = 10 * x + 10 * y
        self.h = width - x + height - y
        self.explored_times = 0

    def __repr__(self):
        return f"Cave Location: ({self.x}, {self.y}) has risk {self.risk} and " \
               f"cost {self.min_cost} with heuristic {self.h}"

    def explore_counter(self, verbose=False):
        self.explored_times = self.explored_times+1
        if (verbose): print(f'We have explored node ({self.x, self.y}) {self.explored_times} times')


class Cave:

    def __init__(self, cave_map):
        self.original_cave_map = cave_map
        self.cave_locations = self.generate_cave_locations(cave_map)
        self.cave_map = self.get_cave_map_risk()
        self.exploration_count = 0
        self.fig, self.ax = plt.subplots(1, 1)
        self.searched_x, self.searched_y = [], []
        self.sc = self.ax.scatter(self.searched_x, self.searched_y, c='red')
        self.image = self.get_cave_map_cost()
        self.im = self.ax.imshow(self.image)
        self.colorbar = range(10)
        self.frontier = []

    def generate_cave_locations(self, cave_map):
        cave_locations = np.ndarray(shape=cave_map.shape, dtype=CaveLocation)
        max_y, max_x = cave_map.shape
        for y in range(max_y):
            for x in range(max_x):
                cave_locations[y, x] = CaveLocation(x, y, max_x, max_y, cave_map[y, x])
        return cave_locations

    def get_cave_map_risk(self, verbose=False):
        cave_map = np.ndarray(shape=self.cave_locations.shape, dtype=int)
        max_y, max_x = self.cave_locations.shape
        for y in range(max_y):
            for x in range(max_x):
                cave_map[y, x] = self.cave_locations[y, x].risk
        if verbose:
            print(cave_map)
        return cave_map

    def get_cave_map_cost(self, verbose=False):
        cave_map = np.ndarray(shape=self.cave_locations.shape, dtype=int)
        max_y, max_x = self.cave_locations.shape
        for y in range(max_y):
            for x in range(max_x):
                cave_map[y, x] = self.cave_locations[y, x].min_cost
        if verbose:
            print(cave_map)
        return cave_map


    def explore_v2(self, current_node):
        self.exploration_count = self.exploration_count + 1
        print(f'We have explored {self.exploration_count} nodes')
        current_node.explore_counter(verbose=True)
        possible_moves = get_possible_moves(current_node.x, current_node.y, self.cave_map)
        print(possible_moves)
        for node_coordinates in possible_moves.values():
            check_node = self.cave_locations[node_coordinates[1], node_coordinates[0]]

    def explore(self, start_x, start_y, end_x, end_y):
        self.exploration_count = self.exploration_count+1
        print(f'We have explored {self.exploration_count} nodes')
        current_node = self.cave_locations[start_y, start_x]
        current_node.explore_counter(verbose=True)
        possible_moves = get_possible_moves(start_x, start_y, self.cave_map)
        for node_coordinates in possible_moves.values():
            check_node = self.cave_locations[node_coordinates[1], node_coordinates[0]]
            if current_node.min_cost + check_node.risk < check_node.min_cost:
                # print(f'Previous min cost of {node_coordinates} was {check_node.min_cost} now'
                #       f'setting to {current_node.min_cost + check_node.risk}')
                check_node.min_cost = current_node.min_cost + check_node.risk
                if node_coordinates[0]<end_x and node_coordinates[1]< end_y:

                    self.explore(node_coordinates[0], node_coordinates[1], end_x, end_y)
        # print(cavern.get_cave_map_cost())
        # Plot here
        self.image = cavern.get_cave_map_cost()
        self.im.set_data(self.image)
        # if self.exploration_count % 10 == 0:
        #     self.searched_x, self.searched_y = [], []
        if len(self.searched_x) > 10:
            self.searched_x.pop(0)
            self.searched_y.pop(0)
        self.searched_x.append(node_coordinates[0])
        self.searched_y.append(node_coordinates[1])
        self.sc.set_offsets(np.c_[self.searched_x, self.searched_y])


        self.fig.canvas.draw_idle()
        # plt.scatter(node_coordinates[0], node_coordinates[1], color='r')
        plt.pause(0.1)


def get_possible_moves(x, y, cave_map):
    y_max, x_max = cave_map.shape
    possible_moves = {}
    possible_moves['down'] = (x, y + 1)
    possible_moves['right'] = (x + 1, y)
    possible_moves['up'] = (x, y - 1)
    possible_moves['left'] = (x - 1, y)
    moves = {}
    for move in possible_moves:
        if (possible_moves[move][0] in range(0, x_max)) and (possible_moves[move][1] in range(0, y_max)):
            moves[move] = possible_moves[move]
    return moves


class Path:
    path_id = 0

    def __init__(self, cave_map, path_list=[(0, 0)]):
        self.__id = Path.path_id
        Path.path_id += 1
        self.__cave_map = cave_map
        self.__path_list = path_list

    def add_move_to_path(self, move):
        current_location = self.__path_list[-1]
        possible_moves = get_possible_moves(current_location[0], current_location[1], self.__cave_map)
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
    testing = True
    cavern_map = LineParser(testing).get_initial_state()



    print("---------------------")
    cavern = Cave(cavern_map)
    # print(cavern_map.shape)


    cavern.get_cave_map_cost(True)

    cavern.explore(0, 0, 100, 100)
    cavern.explore_v2(cavern.cave_locations[0,0])
    cavern.get_cave_map_cost(True)


    # print(cavern.cave_locations)
