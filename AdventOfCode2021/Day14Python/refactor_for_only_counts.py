from datetime import datetime


class LineParser:

    def __init__(self, testing_flag=False, offset=0, separation=12, array_size=10):
        input_data = self.load_input(testing_flag)
        self.initial_state = []
        input_lines = []
        for line in input_data:
            if (line == '\n'):
                self.initial_state.append(input_lines)
                input_lines = []
            else:
                input_lines.append(line.strip())
        self.initial_state.append(input_lines)

    def get_initial_state(self):
        return self.initial_state

    def load_input(self, testing_flag):
        input_path = "./input2.txt"
        if testing_flag:
            input_path = "./sample_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines



# class Rule:
#     def __init__(self, text_input: str):
#         target, insert = text_input.split(" -> ")
#         self.__target = (target[0], target[1])
#         self.__insert = insert
#
#
#     def get_target(self):
#         return self.__target
#
#     def get_insert(self):
#         return self.__inset
#
#     def __eq__(self, other):
#         if isinstance(other, Rule):
#             return self.__hash__() == other.__hash__()
#         else:
#             return False
#
#     def __hash__(self):
#         return hash(self.__repr__())
#
#     def __repr__(self):
#         return f'Rule inserting ({self.__insert} between block {self.__target})'


def add_block_to_template(template, block, times = 1):
    if block in template:
        template[block] += times
    else:
        template[block] = times


def initalise_template(test=False, verbose=False):
    template_text = LineParser(test).get_initial_state()[0][0]
    if verbose:
        print('--------------------------------------------------------------------')
        print('The raw input is: ')
        print(template_text)
        print('Then initalise template:')
    template = {}
    for block_index in range(len(template_text)-1):
        block = template_text[block_index:block_index+2]
        add_block_to_template(template, block)
    if verbose:
        print(template)
        print('--------------------------------------------------------------------')
        print('')
        print('')
    return template

def initalise_rules(test=False, verbose=False):
    point_text = LineParser(test)
    if verbose:
        print('--------------------------------------------------------------------')
        print('The raw input is: ')
        print(point_text.initial_state)
        print('Initalise rules:')
    rule_objects = {}
    for raw_rule in point_text.initial_state[1]:
        target, insert = raw_rule.split(" -> ")
        rule_objects[target] = (target[0]+insert, insert+target[1])
    if verbose:
        print(rule_objects)
        print('--------------------------------------------------------------------')
        print('')
        print('')
    return rule_objects

def apply_rules(template, rules):
    inserts = []
    for pair_index in range(len(template)-1):
        # pair = ''.join([template[pair_index],template[pair_index+1]])
        pair = ''.join([template[pair_index], template[pair_index + 1]])
        if pair in rules:
            inserts.append(rules[pair])
        else:
            inserts.append('')
    new_template = [template[0]]
    for insert_index in range(len(inserts)):
        new_template.append(inserts[insert_index])
        new_template.append(template[insert_index+1])
    return new_template

# The inisight of a "smarter" implelementation, is that for each pair, the output is entirely predicatble. e.g.

if __name__ == '__main__':
    template = initalise_template(True, True)
    rules = initalise_rules(True, True)
    # template = initalise_template()
    # rules = initalise_rules()
    # print(f'Template: {"".join(template)}')
    # for step in range(10):
    #     template = apply_rules(template, rules)
    #     print(f'After step {step+1}: Template is {len(template)} blocks; {"".join(template)}')
    #     print(f'step {step+1} complete the template is now {len(template)} blocks long.')
    #
    #     print(f'{datetime.now()}')
    # unqique_counts = []
    # for unique_block in set(template):
    #     value = sum([True for block in template if block == unique_block])
    #     unqique_counts.append(value)
    #     print(f'Block "{unique_block}" occurs {sum([ True for block in template if block == unique_block])} times')
    # print(f'The difference between the most and least common blocks is {max(unqique_counts)-min(unqique_counts)}')
    # # do_fold(points, folds[0])
    # for fold in folds:
    #     do_fold(points, fold)
    # advent_of_code_print_out(points)