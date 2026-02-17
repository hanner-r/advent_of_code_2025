# The actual password is the number of times the dial is left pointing at 0 after
# any rotation in the sequence

with open('day1_input.txt', 'r') as input_file:
    rotations_list = [line.replace('\n', '') for line in input_file.readlines()]

print(rotations_list)

dial_start_position = 50

def is_dial_position_zero(starting_position, rotation):
    # something recursive?
