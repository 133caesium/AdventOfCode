# I TRIED TO USE SLOTS BUT IT DOESN'T WORK WELL.

class Passport(object):
    def __init__(self, **kwargs):
        try:
            self._byr = kwargs.get('byr')
        except:
            print("error found, passing")
        self.__iyr = kwargs.get('iyr')
        self.__eyr = kwargs.get('eyr')
        self.__hgt = kwargs.get('hgt')
        self.__hcl = kwargs.get('hcl')
        self.__ecl = kwargs.get('ecl')
        self.__pid = kwargs.get('pid')
        self.__cid = kwargs.get('cid')

    def is_valid(self):
        properties = [self._byr, self.__iyr, self.__eyr, self.__hgt, self.__hcl, self.__ecl, self.__pid, self.__cid]
        for value in properties:
            if value==None:
                return False
        return True

    def is_valid_cid_optional(self):
        properties = [self._byr, self.__iyr, self.__eyr, self.__hgt, self.__hcl, self.__ecl, self.__pid]
        for value in properties:
            if value==None:
                return False
        return True

    @property
    def _byr(self):
        return self.__byr

    @_byr.setter
    def _byr(self, value):
        self.__byr = value
        if value==None:
            self.__byr = None
        elif len(str(value)) != 4:
            self.__byr = None
            raise ValueError("byr value has incorrect length")
        else:
            value = int(value)
            if 1919 < value < 2003:
                self.__byr = value
            else:
                self.__byr = None
                raise ValueError("byr was not in range")


class Passport_from_dict(Passport):
     def __init__(self, **kwargs):
         super().__init__(**kwargs)



# class Passport(object):
#     __slots__ = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#
#     def is_valid(self):
#
#
# class Passport_from_dict(Passport):
#     __slots__ = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)



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

