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

def calculate_answer(parser):
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
