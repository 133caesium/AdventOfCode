# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def is_pallindrome(number):
    number_string = str(number)
    reverse_number_string = number_string[::-1]
    return str(number) == reverse_number_string[::-1]

def check_for_square_pallindromes():
    for number in range(10000):
        if is_pallindrome(number**2):
            print(f'The number {number} when squared gives pallindrome {number**2}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [number for number in range(1000) if str(number ** 2) == str(number ** 2)[::-1]]
    for number in numbers:
        print(f'{number} squared gives {number**2} which is a pallindrome')




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
