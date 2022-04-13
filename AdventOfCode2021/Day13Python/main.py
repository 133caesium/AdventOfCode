import numpy as np


class LineParser:

    def __init__(self, testing_flag=False, offset=0, separation=12, array_size=10):
        input_data = self.load_input(testing_flag)
        self.initial_state = []
        input_lines = []
        for line in input_data:
            if (line == '\n'):
                self.initial_state.append(input_lines)
                input_lines = []
            else:
                input_lines.append(line.strip())
        self.initial_state.append(input_lines)

    def get_initial_state(self):
        return self.initial_state

    def load_input(self, testing_flag):
        input_path = "./input.txt"
        if testing_flag:
            input_path = "./sample_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines



class Cooridante:
    def __init__(self, text_input: str):
        x_coordinate_text, y_coordinate_text = text_input.split(",")
        self.__x_cordinate = int(x_coordinate_text)
        self.__y_cordinate = int(y_coordinate_text)

    def fold_y(self, y_fold_line):
        if self.__y_cordinate>= y_fold_line:
            self.__y_cordinate = 2*y_fold_line - self.__y_cordinate

    def fold_x(self, x_fold_line):
        if self.__x_cordinate>= x_fold_line:
            self.__x_cordinate = 2*x_fold_line - self.__x_cordinate


    def get_x(self):
        return self.__x_cordinate

    def get_y(self):
        return self.__y_cordinate

    def get_x_y(self):
        return (self.__x_cordinate, self.__y_cordinate)

    def __eq__(self, other):
        if isinstance(other, Cooridante):
            return self.__hash__() == other.__hash__()
        else:
            return False

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return f'Point at ({self.__x_cordinate},{self.__y_cordinate})'


def initalise_points(test=False, verbose=False):
    point_text = LineParser(test)
    if verbose:
        print('--------------------------------------------------------------------')
        print('The raw input is: ')
        print(point_text.initial_state)
        print('First initalise points:')
    point_objects = []
    for raw_point in point_text.initial_state[0]:
        new_point = Cooridante(raw_point)
        point_objects.append(new_point)
    if verbose:
        print(point_objects)
        print('--------------------------------------------------------------------')
        print('')
        print('')
    return point_objects

def initalise_folds(test=False, verbose=False):
    point_text = LineParser(test)
    if verbose:
        print('--------------------------------------------------------------------')
        print('The raw input is: ')
        print(point_text.initial_state[1])
        print('Then initalise folds:')
    fold_objects = []
    for fold in point_text.initial_state[1]:
        raw_fold = fold.split(" ")[2].split("=")
        fold_objects.append(raw_fold)
    if verbose:
        print(fold_objects)
        print('--------------------------------------------------------------------')
        print('')
        print('')
    return fold_objects

def advent_of_code_print_out(points):
    max_x = 0
    max_y = 0
    for point in points:
        if point.get_x() > max_x:
            max_x = point.get_x()
        if point.get_y() > max_y:
            max_y = point.get_y()
    sheet = np.zeros((max_y + 1, max_x + 1))

    for point in points:
        sheet[point.get_y(), point.get_x()] = True

    print('--------------------------------------------------------------------')
    for row in sheet:
        row_string = ""
        for cell in row:
            if cell>0:
                row_string += '#'
            else:
                row_string += '.'
        print(row_string)
    print(f'The total number of points is {sheet.sum()}')
    print('--------------------------------------------------------------------')

def do_fold(points, fold):
    for point in points:
        if fold[0]=='x':
            point.fold_x(int(fold[1]))
        elif fold[0]=='y':
            point.fold_y(int(fold[1]))

if __name__ == '__main__':
    points = initalise_points(False, True)
    folds = initalise_folds(False, True)
    # do_fold(points, folds[0])
    for fold in folds:
        do_fold(points, fold)
    advent_of_code_print_out(points)