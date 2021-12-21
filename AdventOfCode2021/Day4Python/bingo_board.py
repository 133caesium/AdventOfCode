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
        inital_index = colIndex * 5
        current_index = inital_index
        col_is_complete = True
        while current_index < len(self.__called):
            if not self.__called[current_index]:
                col_is_complete = False
            current_index = current_index + 5
        return col_is_complete

    def add_called_number(self, calledNumber):
        if calledNumber in self.__board:
            number_index = self.__board.index(calledNumber)
            self.__called[number_index] = True

