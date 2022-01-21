class NaviLine:

    def __init__(self, input_string):
        self.__original_string = input_string
        self.__simplified_string = input_string

        self.__count_square_open = self.count_bracket("[")
        self.__count_square_close = self.count_bracket("]")
        self.__count_curly_open = self.count_bracket("{")
        self.__count_curly_closed = self.count_bracket("}")
        self.__count_normal_open = self.count_bracket("(")
        self.__count_normal_closed = self.count_bracket(")")
        self.__count_angle_open = self.count_bracket("<")
        self.__count_angle_closed = self.count_bracket(">")

    def simplify_loop(self):
        continue_loop = True
        while continue_loop:
            characters_removed = 0
            characters_removed += test_string.chain_remove_bracket("[]")
            characters_removed += test_string.chain_remove_bracket("()")
            characters_removed += test_string.chain_remove_bracket("<>")
            characters_removed += test_string.chain_remove_bracket("{}")
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
            print("removing {} from simplified string at index {}".format(character, index))
            print(self.__simplified_string)
            self.__simplified_string = self.__simplified_string[0:index]+self.__simplified_string[index+len(character):]
            print(self.__simplified_string)
            removal = True
        return removal

    def get_original_string(self):
        return self.__original_string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_string = NaviLine('[<>({}){}[([])<>]]')
    test_string.simplify_loop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
