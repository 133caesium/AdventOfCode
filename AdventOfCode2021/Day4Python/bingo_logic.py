def play_bingo(draws, boards):
    bingo = False
    draw_index = 0
    while draw_index < len(draws):
        current_draw = draws[draw_index]
        for board in boards:
            board.add_called_number(current_draw)
            if board.check_all_for_bingo():
                bingo = True
                print("bingo on board {}, from drawing {}, this was draw {}".format(boards.index(board) + 1, current_draw, draw_index))
                break
        else:
            draw_index = draw_index + 1
            continue
        break
    return draw_index

def calculate_answer_first_board_to_win(parser):
    draws = parser.get_draw_numbers()
    boards = parser.get_boards()
    answer = 0
    bingo = False
    draw_index = 0
    while draw_index < len(draws):
        current_draw = draws[draw_index]
        for board in boards:
            board.add_called_number(current_draw)
            if board.check_all_for_bingo():
                bingo = True
                print("bingo on board {}, from drawing {}, this was draw {}".format(boards.index(board) + 1, current_draw, draw_index))
                sum_unmarked = board.get_sum_unmarked()
                print("the sum of unmarked numbers is {}".format(sum_unmarked))
                answer = sum_unmarked*current_draw
                break
        else:
            draw_index = draw_index + 1
            continue
        break
    return answer

def find_last_board_to_bingo(parser):
    draws = parser.get_draw_numbers()
    boards = parser.get_boards()
    answer = 0
    bingo = False
    draw_index = 0
    while draw_index < len(draws):
        boards_with_bingo = 0
        current_draw = draws[draw_index]
        for board in boards:
            board.add_called_number(current_draw)
            if board.check_all_for_bingo():
                boards_with_bingo = boards_with_bingo + 1
            if boards_with_bingo == (len(boards)-1):
                for board in boards:
                    if not board.check_all_for_bingo():
                        print("last board to bingo is board {}".format(boards.index(board) + 1))
                        return (boards.index(board)+1)
        else:
            draw_index = draw_index + 1
            continue
        break

def calculate_answer_to_last_board(parser, last_board):
    draws = parser.get_draw_numbers()
    board = parser.get_boards()[last_board-1]
    answer = 0
    bingo = False
    draw_index = 0
    while draw_index < len(draws):
        current_draw = draws[draw_index]
        board.add_called_number(current_draw)
        if board.check_all_for_bingo():
            bingo = True
            print("bingo on board {}, from drawing {}, this was draw {}".format(last_board, current_draw, draw_index))
            sum_unmarked = board.get_sum_unmarked()
            print("the sum of unmarked numbers is {}".format(sum_unmarked))
            answer = sum_unmarked*current_draw
            break
        else:
            draw_index = draw_index + 1
            continue
        break
    return answer
