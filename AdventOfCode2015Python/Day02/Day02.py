from Utilities.Utilities import LineParser

testing = True
raw_input = LineParser(False)


class Present:

    def __init__(self, present_string):
        self.present_string = present_string.strip().split("x")
        self.present_string_numbers = []
        for number in self.present_string:
            self.present_string_numbers.append(int(number))
        self.present_string_numbers.sort()
        self.wrap_area = 3*self.present_string_numbers[0]*self.present_string_numbers[1]
        self.wrap_area += 2 * self.present_string_numbers[0] * self.present_string_numbers[2]
        self.wrap_area += 2 * self.present_string_numbers[1] * self.present_string_numbers[2]
        self.ribbon = 2*(self.present_string_numbers[0]+self.present_string_numbers[1])+self.present_string_numbers[0]*self.present_string_numbers[1]*self.present_string_numbers[2]


if __name__ == '__main__':
    test_input = raw_input.get_initial_state()
    total = 0
    for input in test_input:
        present = Present(input)
        total += present.ribbon
    print(total)