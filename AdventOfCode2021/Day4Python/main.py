import bingoparser
import bingo_board
import bingo_logic


def day4_part1():
    parser = bingoparser.BingoParser()
    # draws = parser.get_draw_numbers()
    # boards = parser.get_boards()
    # bingo_logic.play_bingo(draws,boards)
    answer = bingo_logic.calculate_answer_first_board_to_win(parser)
    print(answer)


def day4_part2():
    parser = bingoparser.BingoParser()
    last_board = bingo_logic.find_last_board_to_bingo(parser)
    answer = bingo_logic.calculate_answer_to_last_board(parser, last_board)
    print(answer)


if __name__ == '__main__':
    day4_part1()
    day4_part2()
