import bingoparser
import bingo_board
import bingo_logic

def day4():
    parser = bingoparser.BingoParser()
    draws = parser.get_draw_numbers()
    boards = parser.get_boards()
    # bingo_logic.play_bingo(draws,boards)
    answer = bingo_logic.calculate_answer(parser)
    print(answer)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day4()
