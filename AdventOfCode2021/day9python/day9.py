import numpy as np


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
        input_path = "../day9python/input.txt"
        if testing_flag:
            input_path = "../day9python/test_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines


class SmokeMap:
    def __init__(self, parser):
        self.__smoke_map = np.matrix(parser.get_initial_state())
        self.__lowpoint_map = np.zeros(self.__smoke_map.shape, dtype=np.int32)
        self.__basin_map = np.zeros(self.__smoke_map.shape, dtype=np.int32)
        self.__y_max = self.__smoke_map.shape[0] - 1
        self.__x_max = self.__smoke_map.shape[1] - 1
        self.map_lowpoints()
        self.map_basin()
        self.__lowpoint_count = 0


    def get_smoke_map(self):
        return self.__smoke_map

    def get_lowpoint_map(self):
        return self.__lowpoint_map

    def get_basin_map(self):
        return self.__basin_map

    def map_basin(self):
        #if the cell has value 9, it is not in a basin
        #if the cell has an adjacent value that is in a basin, take that value
        #otherwise, increment the basin counter and that cell is in a basin.

        changed_something = False
        basin_count = 1
        scan_x = 0
        while scan_x <= self.__x_max:
            scan_y = 0
            while scan_y <= self.__y_max:
                if self.__smoke_map[scan_y, scan_x] == 9:
                    self.__basin_map[scan_y, scan_x] = -1
                if self.__smoke_map[scan_y, scan_x] != 9:
                    if self.__basin_map[scan_y-1, scan_x] > 0:
                        self.__basin_map[scan_y, scan_x] = self.__basin_map[scan_y-1, scan_x]
                    elif self.__basin_map[scan_y, scan_x-1] > 0:
                        self.__basin_map[scan_y, scan_x] = self.__basin_map[scan_y, scan_x-1]
                    else:
                        self.__basin_map[scan_y, scan_x] = basin_count
                        basin_count += 1
                scan_y += 1
            scan_x += 1

    def check_cells_basin(self):
        pass
        #check cell values


    def map_lowpoints(self):
        self.map_corners()
        self.map_edges()
        self.map_center()

    def map_center(self):
        scan_x = 1
        while scan_x < self.__x_max:
            scan_y = 1
            while scan_y < self.__y_max:
                if self.check_above_higher(scan_y, scan_x) and self.check_left_higher(scan_y, scan_x) and self.check_right_higher(scan_y, scan_x) and self.check_below_higher(scan_y, scan_x):
                    self.__lowpoint_map[scan_y, scan_x] = self.__smoke_map[scan_y, scan_x] + 1
                scan_y += 1
            scan_x += 1

    def map_edges(self):
        scan_x = 1
        while scan_x < self.__x_max:
            if self.check_left_higher(0, scan_x) and self.check_right_higher(0, scan_x) and self.check_below_higher(0, scan_x):
                self.__lowpoint_map[0, scan_x] = self.__smoke_map[0, scan_x] + 1
            if self.check_left_higher(self.__y_max, scan_x) and self.check_right_higher(self.__y_max, scan_x) and self.check_above_higher(self.__y_max, scan_x):
                self.__lowpoint_map[self.__y_max, scan_x] = self.__smoke_map[self.__y_max, scan_x] + 1
            scan_x += 1

        scan_y = 1
        while scan_y < self.__y_max:
            if self.check_above_higher(scan_y, 0) and self.check_right_higher(scan_y, 0) and self.check_below_higher(scan_y, 0):
                self.__lowpoint_map[scan_y, 0] = self.__smoke_map[scan_y, 0] + 1
            if self.check_above_higher(scan_y, self.__x_max) and self.check_left_higher(scan_y, self.__x_max) and self.check_below_higher(
                    scan_y, self.__x_max):
                self.__lowpoint_map[scan_y, self.__x_max] = self.__smoke_map[scan_y, self.__x_max] + 1
            scan_y += 1

    def map_corners(self):
        if self.check_right_higher(0,0) and self.check_below_higher(0,0):
            self.__lowpoint_map[0,0] = self.__smoke_map[0,0]+1
        if self.check_left_higher(0,self.__x_max) and self.check_below_higher(0,self.__x_max):
            self.__lowpoint_map[0,self.__x_max] = self.__smoke_map[0,self.__x_max]+1
        if self.check_right_higher(self.__y_max,0) and self.check_above_higher(self.__y_max,0):
            self.__lowpoint_map[self.__y_max,0] = self.__smoke_map[self.__y_max,0]+1
        if self.check_left_higher(self.__y_max, self.__x_max) and self.check_above_higher(self.__y_max, self.__x_max):
            self.__lowpoint_map[self.__y_max, self.__x_max] = self.__smoke_map[self.__y_max, self.__x_max] + 1

    def check_above_higher(self,y,x):
        return self.__smoke_map[y,x]<self.__smoke_map[y-1,x]

    def check_left_higher(self,y,x):
        return self.__smoke_map[y,x]<self.__smoke_map[y,x-1]

    def check_right_higher(self, y, x):
        return self.__smoke_map[y, x] < self.__smoke_map[y, x+1]

    def check_below_higher(self, y, x):
        return self.__smoke_map[y, x] < self.__smoke_map[y +1, x]


if __name__ == '__main__':
    parser = LineParser(True)
    smoke_map = SmokeMap(parser)
    print(smoke_map.get_smoke_map())
    print(smoke_map.get_lowpoint_map())
    print(smoke_map.get_lowpoint_map().sum())
    print(smoke_map.get_basin_map())



