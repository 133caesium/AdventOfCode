from passport_module import Passport, Passport_from_dict

class passport_parser:
    def __init__(self):
        input_data = self.load_input()
        self.__passport_list = []
        self.__passport_data = {}
        for line in input_data:
            if line == '\n':
                self.make_passport()
            else:
                passport_properties = line.split()
                for passport_property in passport_properties:
                    self.__passport_data[passport_property[0:3]] = passport_property[4:]
        self.make_passport()

    def get_passports(self):
        return self.__passport_list

    def make_passport(self):
        self.__passport_list.append(Passport_from_dict(**self.__passport_data))
        self.__passport_data = {}

    def load_input(self):
        input_lines = []
        with open('./resources/input.txt') as file:
            input_lines = file.readlines()
        return input_lines


###
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
###