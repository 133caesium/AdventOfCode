from Utilities.Utilities import LineParser

testing = True
raw_input = LineParser(False)


if __name__ == '__main__':
    initial_level = 0
    for letter in raw_input.get_initial_state()[0]:
        if (letter == '('):
            initial_level += 1
        else:
            initial_level -= 1
    print(initial_level)
    index = 0
    initial_level = 0
    while initial_level >=0:
        if (raw_input.get_initial_state()[0][index] == '('):
            initial_level += 1
        else:
            initial_level -= 1
        index += 1
    print(index)