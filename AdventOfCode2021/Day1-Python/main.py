from sonar_parser import sonar_parser

###
# Code that solves the puzzle from Advent of Code 2021
# URL: https://adventofcode.com/2021/day/1
###

def main():
    sonar = sonar_parser()
    depth_increases = sonar.get_depth_increases(3)
    print(f'The number of depth increases is {depth_increases}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    main()