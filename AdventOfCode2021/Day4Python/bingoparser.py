class BingoParser:

    def __init__(self, testing_flag=False):
        input_data = self.load_input(testing_flag)
        self.__draw_numbers = self.draw_numbers_from_input(input_data)
        self.__boards = self.boards_from_input(input_data)

    def get_draw_numbers(self):
        return self.__draw_numbers

    def load_input(self, testing_flag):
        input_lines = []
        input_path = "./input.txt"
        if testing_flag:
            input_path = "./test_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines

    def draw_numbers_from_input(self, input_data):
        draw_numbers = input_data[0].strip().split(",")
        draw_numbers_as_int = [int(numeric_string) for numeric_string in draw_numbers]
        return draw_numbers_as_int

    def boards_from_input(self, input_data):
        return []

def board_list_from_strings(board_list):
    test_board_list = []
    for row in board_list:
        row_list = row.split()
        for number in row_list:
            test_board_list.append(int(number))
    return test_board_list
