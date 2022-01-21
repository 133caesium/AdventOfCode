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
        self.__y_max = self.__smoke_map.shape[0] - 1
        self.__x_max = self.__smoke_map.shape[1] - 1
        self.map_lowpoints()
        self.__lowpoint_count = 0


    def get_smoke_map(self):
        return self.__smoke_map

    def get_lowpoint_map(self):
        return self.__lowpoint_map

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

    # def plot_vertical_line(self, lineCoordinates):
    #     current_y = min(lineCoordinates.get_y1(), lineCoordinates.get_y2())
    #     final_y = max(lineCoordinates.get_y1(), lineCoordinates.get_y2()) + 1
    #     line_x = lineCoordinates.get_x1()
    #     while current_y < final_y:
    #         self.__hydrothermal_map_matrix[line_x, current_y] += 1
    #         current_y += 1
    #
    # def plot_horizontal_line(self, lineCoordinates):
    #     current_x = min(lineCoordinates.get_x1(), lineCoordinates.get_x2())
    #     final_x = max(lineCoordinates.get_x1(), lineCoordinates.get_x2()) + 1
    #     line_y = lineCoordinates.get_y1()
    #     while current_x < final_x:
    #         self.__hydrothermal_map_matrix[current_x, line_y] += 1
    #         current_x += 1

    # def plot_diagonal_up(self, lineCoordinates):
    #     current_x = min(lineCoordinates.get_x1(), lineCoordinates.get_x2())
    #     final_x = max(lineCoordinates.get_x1(), lineCoordinates.get_x2()) + 1
    #     current_y = min(lineCoordinates.get_y1(), lineCoordinates.get_y2())
    #     while current_x < final_x:
    #         self.__hydrothermal_map_matrix[current_x, current_y] += 1
    #         current_x += 1
    #         current_y += 1

    # def plot_diagonal_down(self, lineCoordinates):
    #     current_x = min(lineCoordinates.get_x1(), lineCoordinates.get_x2())
    #     final_x = max(lineCoordinates.get_x1(), lineCoordinates.get_x2()) + 1
    #     current_y = max(lineCoordinates.get_y1(), lineCoordinates.get_y2())
    #     while current_x < final_x:
    #         self.__hydrothermal_map_matrix[current_x, current_y] += 1
    #         current_x += 1
    #         current_y -= 1
    #
    # def plot_all_lines(self):
    #     for coordinates in self.__line_coordinates:
    #         if coordinates.get_vertical():
    #             self.plot_vertical_line(coordinates)
    #         elif coordinates.get_horizontal():
    #             self.plot_horizontal_line(coordinates)
    #         elif coordinates.get_diagonal_down():
    #             self.plot_diagonal_down(coordinates)
    #         elif coordinates.get_diagonal_up():
    #             self.plot_diagonal_up(coordinates)
    #         else:
    #             pass

# class LineCoordinates:
#     def __init__(self, line):
#         self.__x1 = int(line.split()[0].split(",")[0])
#         self.__y1 = int(line.split()[0].split(",")[1])
#         self.__x2 = int(line.split()[2].split(",")[0])
#         self.__y2 = int(line.split()[2].split(",")[1])
#         self.__vertical = False
#         self.__horizontal = False
#         self.__diagonal_up = False
#         self.__diagonal_down = False
#
#         if self.__x1 == self.__x2:
#             self.__vertical = True
#         if self.__y1 == self.__y2:
#             self.__horizontal = True
#         if (self.__x2-self.__x1)==(self.__y2-self.__y1):
#             self.__diagonal_up = True
#         if (self.__x2-self.__x1)==(self.__y1-self.__y2):
#             self.__diagonal_down = True
#
#
#     def get_x1(self):
#         return self.__x1
#
#     def get_x2(self):
#         return self.__x2
#
#     def get_y1(self):
#         return self.__y1
#
#     def get_y2(self):
#         return self.__y2
#
#     def get_horizontal(self):
#         return self.__horizontal
#
#     def get_vertical(self):
#         return self.__vertical
#
#     def get_diagonal_up(self):
#         return self.__diagonal_up
#
#     def get_diagonal_down(self):
#         return self.__diagonal_down



if __name__ == '__main__':
    parser = LineParser()
    smoke_map = SmokeMap(parser)
    print(smoke_map.get_smoke_map())
    print(smoke_map.get_lowpoint_map())
    print(smoke_map.get_lowpoint_map().sum())



