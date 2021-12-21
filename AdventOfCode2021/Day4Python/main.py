from bingoparser import BingoParser

def day4():
    bingo_data = BingoParser(True)
    print(bingo_data.get_draw_numbers())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day4()
