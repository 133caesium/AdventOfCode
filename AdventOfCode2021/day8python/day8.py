import unittest

class SevenSegmentInput:
    def __init__(self, input_line):
        self.example_numbers = input_line[0:10]
        self.unknown_numbers = input_line[11:15]
        self.decoded_numbers = []
        self.number_mapping_key = {}

    def decode_one(self):
        for coded_number in self.example_numbers:
            if len(coded_number)==2:
                self.number_mapping_key[coded_number] = 1



class LineParser:

    def __init__(self, testing_flag=False):
        input_data = self.load_input(testing_flag)
        # input_strings=input_data[0].split(",")
        self.initial_state = []
        for line in input_data:
            self.initial_state.append(line.split())

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

if __name__ == '__main__':
    parser = LineParser(True)
    for line in parser.get_initial_state():
        seven_segment = SevenSegmentInput(line)
        seven_segment.decode_one()
        print(seven_segment.example_numbers)
        print(seven_segment.unknown_numbers)
        print(seven_segment.number_mapping_key)


