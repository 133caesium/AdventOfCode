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
        self.__lowpoint_map = self.map_lowpoints()
        self.__lowpoint_count = 0
        # self.__y_dimension = parser.get_max_y()+1
        # self.__hydrothermal_map_matrix = np.zeros((self.__x_dimension, self.__y_dimension), dtype=np.int32)
        # self.__line_coordinates = parser.get_lines()

    def get_map(self):
        return self.__smoke_map

    def map_lowpoints(self):
        new_map = np.zeros(self.__smoke_map.shape, dtype=np.int32)
        return new_map


    def map(self):
        pass

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
    parser = LineParser(True)
    smoke_map = SmokeMap(parser)
    print(smoke_map.get_map())
    print(np.zeros(smoke_map.get_map().shape, dtype=np.int32))


