class LineParser:

    def __init__(self, testing_flag=False):
        input_data = self.load_input(testing_flag)
        self.initial_state = input_data

    def get_initial_state(self):
        return self.initial_state

    def load_input(self, testing_flag):
        input_path = "./input.txt"
        if testing_flag:
            input_path = "./sample_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines
