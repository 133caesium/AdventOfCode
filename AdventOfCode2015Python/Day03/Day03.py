import copy

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

    def move(self, move):
        if move == '^':
            self.y += 1
        elif move == 'v':
            self.y -= 1
        elif move == '>':
            self.x += 1
        elif move == '<':
            self.x -= 1
        else:
            print('Error, unexpected move')


#     https://www.singlelunch.com/2018/09/26/programming-trick-cantor-pairing-perfect-hashing-of-two-integers/


if __name__ == '__main__':
    print(f'We will test {len(raw_input.get_initial_state()[0])} moves')

    # Day 03 Part 1
    santa = CartesianLocation(0, 0)
    visited_locations = {santa}
    for move in raw_input.get_initial_state()[0]:
        santa.move(move)
        visited_locations.add(copy.copy(santa))
    print(f'Day03 Part 1: We have visited {len(visited_locations)} locations')

    # Day 03 Part 2
    santa = CartesianLocation(0, 0)
    roboSanta = CartesianLocation(0, 0)
    visited_locations = {santa}
    for move in raw_input.get_initial_state()[0][0::2]:
        santa.move(move)
        visited_locations.add(copy.copy(santa))
    for move in raw_input.get_initial_state()[0][1::2]:
        roboSanta.move(move)
        visited_locations.add(copy.copy(roboSanta))
    print(f'Day03 Part 2: We have visited {len(visited_locations)} locations')

