class LineParser:

    def __init__(self, testing_flag=False):
        input_data = self.load_input(testing_flag)
        # input_strings=input_data[0].split(",")
        self.initial_state = []
        for input_line in input_data:
            output_line = NaviLine(input_line.strip())
            self.initial_state.append(output_line)

    def get_initial_state(self):
        return self.initial_state

    def load_input(self, testing_flag):
        input_path = "./input.txt"
        if testing_flag:
            input_path = "./test_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines

class NaviLine:

    def __init__(self, input_string):
        self.__original_string = input_string
        self.__simplified_string = input_string
        #
        # self.__count_square_open = self.count_bracket("[")
        # self.__count_square_close = self.count_bracket("]")
        # self.__count_curly_open = self.count_bracket("{")
        # self.__count_curly_closed = self.count_bracket("}")
        # self.__count_normal_open = self.count_bracket("(")
        # self.__count_normal_closed = self.count_bracket(")")
        # self.__count_angle_open = self.count_bracket("<")
        # self.__count_angle_closed = self.count_bracket(">")

        self.simplify_loop()

        self.__first_illegal = None
        self.__first_illegal_index = len(input_string)
        self.find_illegal()

    def find_illegal(self):
        possible_illegal_characters = ']})>'
        for character in possible_illegal_characters:
            if character in self.__simplified_string:
                if self.__simplified_string.index(character) < self.__first_illegal_index:
                    self.__first_illegal_index = self.__simplified_string.index(character)
                    self.__first_illegal = character


    def simplify_loop(self):
        continue_loop = True
        while continue_loop:
            characters_removed = 0
            characters_removed += self.chain_remove_bracket("[]")
            characters_removed += self.chain_remove_bracket("()")
            characters_removed += self.chain_remove_bracket("<>")
            characters_removed += self.chain_remove_bracket("{}")
            if characters_removed == 0:
                continue_loop = False


    def chain_remove_bracket(self, character):
        more_to_remove = True
        characters_removed = -1
        while more_to_remove:
            more_to_remove = self.remove_character(character)
            characters_removed += 1
        return characters_removed

    def count_bracket(self, bracket):
        count = 0
        for character in self.__simplified_string:
            if character == bracket:
                count += 1
        return count

    def remove_character(self, character):
        removal = False
        if character in self.__simplified_string:
            index = self.__simplified_string.index(character)
            # print("removing {} from simplified string at index {}".format(character, index))
            # print(self.__simplified_string)
            self.__simplified_string = self.__simplified_string[0:index]+self.__simplified_string[index+len(character):]
            # print(self.__simplified_string)
            removal = True
        return removal

    def get_original_string(self):
        return self.__original_string

    def get_simplified_string(self):
        return self.__simplified_string

    def get_first_illegal(self):
        return self.__first_illegal


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    syntax_scoring_data = LineParser().get_initial_state()
    syntax_error_score = 0

    for line in syntax_scoring_data:
        print(line.get_original_string())
        print(line.get_simplified_string())
        illegal_character = line.get_first_illegal()
        print(line.get_first_illegal())
        if illegal_character == ')':
            syntax_error_score += 3
        elif illegal_character == ']':
            syntax_error_score += 57
        elif illegal_character == '}':
            syntax_error_score += 1197
        elif illegal_character == '>':
            syntax_error_score += 25137
        if illegal_character:
            print(syntax_error_score)


    # test_string = NaviLine('[<>({}){}[([])<>]]')
    # test_string.simplify_loop()
    print(len(syntax_scoring_data))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
