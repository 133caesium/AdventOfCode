# I TRIED TO USE SLOTS BUT IT DOESN'T WORK WELL.
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

