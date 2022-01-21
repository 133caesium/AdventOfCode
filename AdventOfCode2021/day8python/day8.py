class SevenSegmentInput:
    def __init__(self, input_line):
        self.example_numbers = input_line[0:10]
        self.unknown_numbers = input_line[11:15]
        self.decoded_numbers = []
        self.number_mapping_key = {}
        self.number_list = []
        for index in range(10):
            self.number_list.append(None)
        self.decode_all_numbers()
        # self.decode_unique_numbers()
        self.find_unknown_numbers()

    def find_unknown_numbers(self):
        for number in self.unknown_numbers:
            if number in self.number_mapping_key:
                self.decoded_numbers.append(self.number_mapping_key[number])

    def decode_all_numbers(self):
        self.decode_one()
        self.decode_four()
        self.decode_seven()
        self.decode_eight()

        self.decode_three()
        self.decode_nine()
        self.decode_six()
        self.decode_five()
        self.decode_zero()
        self.decode_two()

    def decode_unique_numbers(self):
        self.decode_one()
        self.decode_four()
        self.decode_seven()
        self.decode_eight()

    def overlaps(self, overlapped, overlapping):
        count_overlapped_letters = 0
        for letter in overlapped:
            if letter in overlapping:
                count_overlapped_letters += 1
        return (len(overlapped)==count_overlapped_letters)

    def decode_zero(self):
        for coded_number in self.example_numbers:
            if len(coded_number) == 6 and coded_number!=self.number_list[6] and coded_number!=self.number_list[9]:
                self.number_mapping_key[coded_number] = 0
                self.number_list[0] = coded_number
                return coded_number

    def decode_one(self):
        for coded_number in self.example_numbers:
            if len(coded_number) == 2:
                self.number_mapping_key[coded_number] = 1
                self.number_list[1] = coded_number
                return coded_number

    def decode_two(self):
        for coded_number in self.example_numbers:
            if not(coded_number in self.number_mapping_key):
                self.number_mapping_key[coded_number] = 2
                self.number_list[2] = coded_number

    def decode_three(self):
        one_character = self.number_list[1]
        for coded_number in self.example_numbers:
            if len(coded_number) == 5 and self.overlaps(one_character, coded_number):
                self.number_mapping_key[coded_number] = 3
                self.number_list[3] = coded_number
                return coded_number

    def decode_four(self):
        for coded_number in self.example_numbers:
            if len(coded_number) == 4:
                self.number_mapping_key[coded_number] = 4
                self.number_list[4] = coded_number
                return coded_number

    def decode_five(self):
        for coded_number in self.example_numbers:
            if len(coded_number) == 5 and self.overlaps(coded_number, self.number_list[6]) and self.overlaps(coded_number, self.number_list[9]):
                self.number_mapping_key[coded_number] = 5
                self.number_list[5] = coded_number
                return coded_number

    def decode_six(self):
        for coded_number in self.example_numbers:
            if len(coded_number) == 6 and not(self.overlaps(self.number_list[1], coded_number)):
                self.number_mapping_key[coded_number] = 6
                self.number_list[6] = coded_number
                return coded_number

    def decode_seven(self):
        for coded_number in self.example_numbers:
            if len(coded_number) == 3:
                self.number_mapping_key[coded_number] = 7
                self.number_list[7] = coded_number
                return coded_number

    def decode_eight(self):
        for coded_number in self.example_numbers:
            if len(coded_number) == 7:
                self.number_mapping_key[coded_number] = 8
                self.number_list[8] = coded_number
                return coded_number

    def decode_nine(self):
        for coded_number in self.example_numbers:
            if len(coded_number) == 6 and self.overlaps(self.number_list[4], coded_number):
                self.number_mapping_key[coded_number] = 9
                self.number_list[9] = coded_number
                return coded_number


class LineParser:

    def __init__(self, testing_flag=False):
        input_data = self.load_input(testing_flag)
        # input_strings=input_data[0].split(",")
        self.initial_state = []
        for input_line in input_data:
            output_line = []
            for number in input_line.split():
                output_line.append(self.sort_string(number))
            self.initial_state.append(output_line)

    def sort_string(self, input_string):
        letters = []
        for letter in input_string:
            letters.append(letter)
        letters.sort()
        output_string = ""
        for letter in letters:
            output_string += letter
        return output_string

    def get_initial_state(self):
        return self.initial_state

    def load_input(self, testing_flag):
        input_path = "./input.txt"
        if testing_flag:
            input_path = "./test_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines


if __name__ == '__main__':
    parser = LineParser()
    count_decoded_numbers = 0
    sum_decoded_numbers = 0

    for line in parser.get_initial_state():
        seven_segment = SevenSegmentInput(line)
        # print(seven_segment.example_numbers)
        # print(seven_segment.unknown_numbers)
        # print(seven_segment.number_mapping_key)
        print(seven_segment.decoded_numbers)
        seven_segment_value = 1000*seven_segment.decoded_numbers[0] + 100*seven_segment.decoded_numbers[1] + 10*seven_segment.decoded_numbers[2] + 1*seven_segment.decoded_numbers[3]
        sum_decoded_numbers += seven_segment_value
        print("adding value {} to total giving {}".format(seven_segment_value, sum_decoded_numbers))
        count_decoded_numbers += len(seven_segment.decoded_numbers)
    print("We found {} numbers in total".format(count_decoded_numbers))
