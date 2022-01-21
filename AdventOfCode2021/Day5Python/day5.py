import numpy as np

class HydrothermalMap:
    def __init__(self, parser):
        self.__x_dimension = parser.get_max_x()+1
        self.__y_dimension = parser.get_max_y()+1
        self.__hydrothermal_map_matrix = np.zeros((self.__x_dimension, self.__y_dimension), dtype=np.int32)
        self.__line_coordinates = parser.get_lines()

    def get_map(self):
        return self.__hydrothermal_map_matrix

    def plot_vertical_line(self, lineCoordinates):
        current_y = min(lineCoordinates.get_y1(), lineCoordinates.get_y2())
        final_y = max(lineCoordinates.get_y1(), lineCoordinates.get_y2()) + 1
        line_x = lineCoordinates.get_x1()
        while current_y < final_y:
            self.__hydrothermal_map_matrix[line_x, current_y] += 1
            current_y += 1

    def plot_horizontal_line(self, lineCoordinates):
        current_x = min(lineCoordinates.get_x1(), lineCoordinates.get_x2())
        final_x = max(lineCoordinates.get_x1(), lineCoordinates.get_x2()) + 1
        line_y = lineCoordinates.get_y1()
        while current_x < final_x:
            self.__hydrothermal_map_matrix[current_x, line_y] += 1
            current_x += 1

    def plot_diagonal_up(self, lineCoordinates):
        current_x = min(lineCoordinates.get_x1(), lineCoordinates.get_x2())
        final_x = max(lineCoordinates.get_x1(), lineCoordinates.get_x2()) + 1
        current_y = min(lineCoordinates.get_y1(), lineCoordinates.get_y2())
        while current_x < final_x:
            self.__hydrothermal_map_matrix[current_x, current_y] += 1
            current_x += 1
            current_y += 1

    def plot_diagonal_down(self, lineCoordinates):
        current_x = min(lineCoordinates.get_x1(), lineCoordinates.get_x2())
        final_x = max(lineCoordinates.get_x1(), lineCoordinates.get_x2()) + 1
        current_y = max(lineCoordinates.get_y1(), lineCoordinates.get_y2())
        while current_x < final_x:
            self.__hydrothermal_map_matrix[current_x, current_y] += 1
            current_x += 1
            current_y -= 1

    def plot_all_lines(self):
        for coordinates in self.__line_coordinates:
            if coordinates.get_vertical():
                self.plot_vertical_line(coordinates)
            elif coordinates.get_horizontal():
                self.plot_horizontal_line(coordinates)
            elif coordinates.get_diagonal_down():
                self.plot_diagonal_down(coordinates)
            elif coordinates.get_diagonal_up():
                self.plot_diagonal_up(coordinates)
            else:
                pass

class LineCoordinates:
    def __init__(self, line):
        self.__x1 = int(line.split()[0].split(",")[0])
        self.__y1 = int(line.split()[0].split(",")[1])
        self.__x2 = int(line.split()[2].split(",")[0])
        self.__y2 = int(line.split()[2].split(",")[1])
        self.__vertical = False
        self.__horizontal = False
        self.__diagonal_up = False
        self.__diagonal_down = False

        if self.__x1 == self.__x2:
            self.__vertical = True
        if self.__y1 == self.__y2:
            self.__horizontal = True
        if (self.__x2-self.__x1)==(self.__y2-self.__y1):
            self.__diagonal_up = True
        if (self.__x2-self.__x1)==(self.__y1-self.__y2):
            self.__diagonal_down = True


    def get_x1(self):
        return self.__x1

    def get_x2(self):
        return self.__x2

    def get_y1(self):
        return self.__y1

    def get_y2(self):
        return self.__y2

    def get_horizontal(self):
        return self.__horizontal

    def get_vertical(self):
        return self.__vertical

    def get_diagonal_up(self):
        return self.__diagonal_up

    def get_diagonal_down(self):
        return self.__diagonal_down


class LineParser:

    def __init__(self, testing_flag=False):
        input_data = self.load_input(testing_flag)
        self.__max_x = 0
        self.__max_y = 0
        self.__line_coordinates = []
        for line in input_data:
            line_coordinates = LineCoordinates(line)
            self.check_max_coordinates(line_coordinates)
            self.__line_coordinates.append(line_coordinates)

    def get_max_x(self):
        return self.__max_x

    def get_max_y(self):
        return self.__max_y

    def get_lines(self):
        return self.__line_coordinates

    def check_max_coordinates(self, line_coordinates):
        if line_coordinates.get_x1()>self.__max_x:
            self.__max_x = line_coordinates.get_x1()
        if line_coordinates.get_x2()>self.__max_x:
            self.__max_x = line_coordinates.get_x2()
        if line_coordinates.get_y1()>self.__max_y:
            self.__max_y = line_coordinates.get_y1()
        if line_coordinates.get_y1() > self.__max_y:
            self.__max_y = line_coordinates.get_y1()


    def load_input(self, testing_flag):
        input_lines = []
        input_path = "./input.txt"
        if testing_flag:
            input_path = "./test_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines


if __name__ == '__main__':
    parser = LineParser()
    hydrothermal_map = HydrothermalMap(parser)
    hydrothermal_map.plot_all_lines()
    print(hydrothermal_map.get_map())
    count = 0
    for row in hydrothermal_map.get_map():
        for point in row:
            if point>1:
                count += 1
    print(count)
