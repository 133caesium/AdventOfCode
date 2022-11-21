import time
from Utilities.Utilities import LineParser

testing = True
raw_input = LineParser(False)
special_pairs = ('ab', 'cd', 'pq', 'xy')


class NaughtyOrNiceString:

    def __init__(self, input_string):
        self.input_string = input_string.strip()
        self.vowelCount = 0
        # self.doubleCount = 0
        # self.specialPairCount = 0
        self.has3Vowels = self.count_vowels()>2
        self.has1double = self.count_doubles()>0
        self.hasNoSpecial = self.count_special_pairs()==0
        self.hasSeparatedDoubles = self.count_separated_doubles() > 0
        self.hasDoubleDoubles = self.count_double_doubles() > 0
        self.isNice = self.has3Vowels and self.has1double and self.hasNoSpecial
        self.isNicer = self.hasSeparatedDoubles & self.hasDoubleDoubles

    def count_vowels(self):
        for letter in self.input_string:
            if letter in ('a', 'e', 'i', 'o', 'u'):
                self.vowelCount += 1
        return self.vowelCount

    def count_doubles(self):
        count = 0
        index = 1
        while index<len(self.input_string):
            if (self.input_string[index-1]==self.input_string[index]):
                count += 1
            index += 1
        return count

    def count_special_pairs(self):
        count = 0
        index = 1
        while index < len(self.input_string):
            if self.input_string[index-1:index+1] in special_pairs:
                count += 1
            index += 1
        return count

    def count_separated_doubles(self):
        count = 0
        index = 2
        while index<len(self.input_string):
            if (self.input_string[index-2]==self.input_string[index]):
                count += 1
            index += 1
        return count

    def count_double_doubles(self):
        count = 0
        index = 2
        while index<len(self.input_string):
            if self.input_string[index-2:index] in self.input_string[index:]:
                count += 1
            index += 1
        return count


if __name__ == '__main__':
    start = time.perf_counter_ns()

    niceCount = 0
    nicerCount = 0
    for testString in raw_input.get_initial_state():
        testObject = NaughtyOrNiceString(testString)
        if testObject.isNice:
            niceCount += 1
        if testObject.isNicer:
            nicerCount += 1

    print(f'We counted {niceCount} nice strings')
    print(f'We counted {nicerCount} nicer strings')

    end = time.perf_counter_ns()
    print(f'The time to solve was {(end - start) / 1_000} us')
    print(f'The time to solve was {(end - start) / 1_000_000} ms')