class sonar_parser:
    def __init__(self):
        input_data = self.load_input()
        self.__depths = []
        self.__passport_data = {}
        for line in input_data:
            self.__depths.append(int(line))


    def get_depths(self):
        return self.__depths

    def get_depth_increases(self):
        number_of_depths = len(self.__depths)
        depth_index = 1
        depth_increase_count = 0
        while depth_index<number_of_depths:
            if self.__depths[depth_index]>self.__depths[depth_index-1]:
                depth_increase_count += 1
            depth_index += 1
        return depth_increase_count

    def make_passport(self):
        self.__passport_list.append(Passport_from_dict(**self.__passport_data))
        self.__passport_data = {}

    def load_input(self):
        input_lines = []
        with open('./input.txt') as file:
            input_lines = file.readlines()
        return input_lines