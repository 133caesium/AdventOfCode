import numpy as np
import time
from Utilities.Utilities import LineParser

raw_input = LineParser(False)

class LightGrid:

    def __init__(self):
        self.grid = np.zeros((1000, 1000))

    def perform_instruction(self, instruction):
        for y in range(instruction.start_y, instruction.end_y+1):
            for x in range(instruction.start_x, instruction.end_x+1):
                if instruction.instruction_type == "on":
                    self.grid[y, x] += 1
                elif instruction.instruction_type == "off":
                    if self.grid[y, x]>0:
                        self.grid[y, x] -= 1
                elif instruction.instruction_type == "toggle":
                    self.grid[y,x] += 2
                else:
                    raise Exception(f'Tried to perform invalid instruction "'
                                    f'{instruction.instruction_type}"'
                                    f'. Did you mean to do that?')

    def count_lights_on(self):
        return self.grid.sum()


class Instruction:
    def __init__(self, input):
        input_split = input.strip().split()
        if input_split[0] == 'turn':
            self.instruction_type = input_split[1]
            input_split = input_split[1:]
        elif input_split[0] == 'toggle':
            self.instruction_type = input_split[0]
        else:
            raise Exception(f'Tried to create invalid instruction "{input_split[0]}". Did you mean to do that?')
        self.start_x = int(input_split[1].split(',')[0])
        self.start_y = int(input_split[1].split(',')[1])
        self.end_x = int(input_split[3].split(',')[0])
        self.end_y = int(input_split[3].split(',')[1])


    def __repr__(self):
        return f'Instruction type: {self.instruction_type} from ({self.start_x},{self.start_y}) to ({self.end_x},{self.end_y})'





if __name__ == '__main__':
    start = time.perf_counter_ns()
    grid = LightGrid()
    print(f'Now there are {grid.count_lights_on()} lights on')
    for input in raw_input.get_initial_state():
        # print(input.strip())
        # print(Instruction(input))
        grid.perform_instruction(Instruction(input))
        # print(grid.grid)
        # print(f'Now there are {grid.count_lights_on()} lights on')
    print(f'Now there are {grid.count_lights_on()} lights on')




    end = time.perf_counter_ns()
    print(f'The time to solve was {(end - start) / 1_000} us')
    print(f'The time to solve was {(end - start) / 1_000_000} ms')

    # test_input = raw_input.get_initial_state()
    # total = 0
    # for input in test_input:
    #     present = Present(input)
    #     total += present.ribbon
    # print(total)
