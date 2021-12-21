class BingoBoard:

    def __init__(self, boardList):
        self.__board = boardList
        self.__called = []
        board_index = 0
        while board_index < len(boardList):
            self.__called.append(False)
            board_index = board_index+1

    def check_row_for_bingo(self, rowIndex):
        inital_index = rowIndex * 5
        final_index = inital_index + 5
        current_index = inital_index
        row_is_complete = True
        while current_index < final_index:
            if not self.__called[current_index]:
                row_is_complete = False
            current_index = current_index + 1
        return row_is_complete

    def check_column_for_bingo(self, colIndex):
        inital_index = colIndex
        current_index = inital_index
        col_is_complete = True
        while current_index < len(self.__called):
            if not self.__called[current_index]:
                col_is_complete = False
            current_index = current_index + 5
        return col_is_complete

    def check_all_for_bingo(self):
        row_col_index = 0
        bingo = False
        while row_col_index < 5:
            if self.check_column_for_bingo(row_col_index) or self.check_row_for_bingo(row_col_index):
                bingo = True
            row_col_index = row_col_index + 1
        return bingo

    def add_called_number(self, calledNumber):
        if calledNumber in self.__board:
            number_index = self.__board.index(calledNumber)
            self.__called[number_index] = True

    def get_number(self, index):
        return self.__board[index]

    def get_called(self, index):
        return self.__called[index]

    def get_sum_unmarked(self):
        sum_of_unmarked = 0
        index = 0
        while index < len(self.__board):
            if not self.__called[index]:
                sum_of_unmarked = sum_of_unmarked + self.__board[index]
            index = index + 1
        return sum_of_unmarked


