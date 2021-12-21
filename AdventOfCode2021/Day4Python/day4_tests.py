import unittest
import bingoparser
import bingo_board

class MyTestCase(unittest.TestCase):

    def test_bingo_parser_draw_numbers(self):
        test_draw_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
        parser = bingoparser.BingoParser(True)
        draw_numbers = parser.get_draw_numbers()
        self.assertEqual(test_draw_numbers,draw_numbers)

    def test_bingo_board_creation(self):
        test_board = ["22 13 17 11  0", "8  2 23  4 24", "21  9 14 16  7", "6 10  3 18  5", "1 12 20 15 19"]
        test_board_list = bingoparser.board_list_from_strings(test_board)
        self.assertEqual(len(test_board_list), 25)
        self.assertEqual(test_board_list[0], 22)
        self.assertEqual(test_board_list[10], 21)
        board = bingo_board.BingoBoard(test_board_list)
        self.assertEqual(board.get_number(0), 22)
        self.assertEqual(board.get_number(10), 21)

    def test_bingo_board_row_bingo(self):
        test_board = ["22 13 17 11  0", "8  2 23  4 24", "21  9 14 16  7", "6 10  3 18  5", "1 12 20 15 19"]
        test_board_list = bingoparser.board_list_from_strings(test_board)
        board = bingo_board.BingoBoard(test_board_list)
        self.assertEqual(board.check_row_for_bingo(0), False)
        self.assertEqual(board.check_all_for_bingo(), False)
        board.add_called_number(22)
        board.add_called_number(13)
        board.add_called_number(17)
        board.add_called_number(11)
        board.add_called_number(0)
        self.assertEqual(board.check_row_for_bingo(2), False)
        self.assertEqual(board.check_column_for_bingo(2), False)
        self.assertEqual(board.check_row_for_bingo(0), True)
        self.assertEqual(board.check_all_for_bingo(), True)

    def test_bingo_board_col_bingo(self):
        test_board = ["22 13 17 11  0", "8  2 23  4 24", "21  9 14 16  7", "6 10  3 18  5", "1 12 20 15 19"]
        test_board_list = bingoparser.board_list_from_strings(test_board)
        board = bingo_board.BingoBoard(test_board_list)
        self.assertEqual(board.check_row_for_bingo(0), False)
        self.assertEqual(board.check_all_for_bingo(), False)
        board.add_called_number(13)
        board.add_called_number(2)
        board.add_called_number(9)
        board.add_called_number(10)
        board.add_called_number(12)
        self.assertEqual(board.check_row_for_bingo(2), False)
        self.assertEqual(board.check_column_for_bingo(1), True)
        self.assertEqual(board.check_row_for_bingo(1), False)
        self.assertEqual(board.check_all_for_bingo(), True)

    def test_bingo_logic(self):
        parser = bingoparser.BingoParser(True)
        self.assertEqual(3 , len(parser.get_boards()))


if __name__ == '__main__':
    unittest.main()
