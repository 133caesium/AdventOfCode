from passport_parser import passport_parser

def main():
    parser = passport_parser()
    passports = parser.get_passports()
    count = 0
    for possiblepassport in passports:
        if possiblepassport.is_valid_cid_optional():
            count+=1
    print(count)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
