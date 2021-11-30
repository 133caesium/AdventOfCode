# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def load_input():
    input_lines = []
    with open('./resources/input.txt') as file:
        input_lines = file.readlines()
    return input_lines
    #
    # count = 0
    # for line in lines:
    #     count += 1
    #     print(f'line {count}: {line}')

def main():
    print(load_input())

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
