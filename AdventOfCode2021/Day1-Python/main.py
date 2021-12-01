from sonar_parser import sonar_parser

def main():
    sonar = sonar_parser()
    depth_increases = sonar.get_depth_increases()
    print(f'The number of depth increases is {depth_increases}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
