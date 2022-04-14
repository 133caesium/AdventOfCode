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
        input_path = "./input.txt"
        if testing_flag:
            input_path = "./sample_input.txt"
        with open(input_path) as file:
            input_lines = file.readlines()
        return input_lines


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
    new_template = {}
    for block in template:
        if block in rules:
            add_block_to_template(new_template, rules[block][0], template[block])
            add_block_to_template(new_template, rules[block][1], template[block])
        else:
            add_block_to_template(new_template, block, template[block])
    return new_template

def apply_steps(template, rules, total_steps, verbose=False):
    for step in range(total_steps):
        template = apply_rules(template, rules)
        template_length = 0
        for block in template:
            template_length += template[block]
        if verbose:
            print(f'After step {step+1}: Template is {template_length} blocks; {template}')
            print(f'step {step+1} complete the template is now {template_length} blocks long.')
            print(f'{datetime.now()}')
    return template


def convet_to_monomers(template, total_steps):
    monomers = {}
    max_monomer_count = 0
    min_monomer_count = 2 ** (total_steps * 2)
    for block in template:
        add_block_to_template(monomers, block[0], template[block])
        add_block_to_template(monomers, block[1], template[block])
    monomers[LineParser(use_sample_input).get_initial_state()[0][0][0]] += 1
    monomers[LineParser(use_sample_input).get_initial_state()[0][0][-1]] += 1
    for monomer in monomers:
        monomers[monomer] = monomers[monomer] / 2
        if monomers[monomer] > max_monomer_count:
            max_monomer_count = monomers[monomer]
        if monomers[monomer] < min_monomer_count:
            min_monomer_count = monomers[monomer]
    print(monomers)
    return (monomers, min_monomer_count, max_monomer_count)

if __name__ == '__main__':
    verbose = False
    use_sample_input = False
    total_steps = 40

    template = initalise_template(use_sample_input, verbose)
    rules = initalise_rules(use_sample_input, verbose)

    template = apply_steps(template, rules, total_steps, verbose)

    monomers, min_monomer_count, max_monomer_count = convet_to_monomers(template, total_steps)

    print(f'Max count is {max_monomer_count}, min count is {min_monomer_count}, difference is {max_monomer_count-min_monomer_count}')

# Leaving this for now, the correct answer is 2265039461737
# There needs to be some consideration of the first and last character, leading to a slight variation in count.