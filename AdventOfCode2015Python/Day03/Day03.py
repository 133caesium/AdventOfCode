from Utilities.Utilities import LineParser

testing = True
raw_input = LineParser(False)

class CartesianLocation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __repr__(self):
        return f'Point at (x={self.x},y={self.y})'

    def __hash__(self):
        return hash(f'{self.x},{self.y}')

#     https://www.singlelunch.com/2018/09/26/programming-trick-cantor-pairing-perfect-hashing-of-two-integers/


if __name__ == '__main__':
    print(f'We will test {len(raw_input.get_initial_state()[0])} locations')
    x = 0
    y = 0
    visited_locations = set()
    for move in raw_input.get_initial_state()[0][::2]:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1
        else:
            print('Error, unexpected move')
        current_location = CartesianLocation(x,y)
        # print(f'Move [{move}] gives {CartesianLocation(x,y)}')
        visited_locations.add(current_location)
        # print(visited_locations)
        # print(f'We have visited {len(visited_locations)} locations')

    print(visited_locations)
    print(f'We have visited {len(visited_locations)} locations')

    # for letter in raw_input.get_initial_state()[0]:
    #     if (letter == '('):
    #         initial_level += 1
    #     else:
    #         initial_level -= 1
    # print(initial_level)
    # index = 0
    # initial_level = 0
    # while initial_level >=0:
    #     if (raw_input.get_initial_state()[0][index] == '('):
    #         initial_level += 1
    #     else:
    #         initial_level -= 1
    #     index += 1
    # print(index)