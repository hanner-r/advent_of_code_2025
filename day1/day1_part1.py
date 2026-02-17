# The actual password is the number of times the dial is left pointing at 0 after
# any rotation in the sequence

with open('day1_input.txt', 'r') as input_file:
    rotations_list = [line.replace('\n', '') for line in input_file.readlines()]

print(rotations_list)

dial_start_position = 50
dial_at_zero_count = 0


def is_dial_position_zero(starting_position, rotation):
    if rotation[0] == 'R':
        new_position = starting_position + int(rotation[1:])
        if new_position > 99:
            new_position -= 100
        elif new_position < 0:
            new_position += 100
    else:
        new_position = starting_position - int(rotation[1:])
        if new_position > 99:
            new_position -= 100
        elif new_position < 0:
            new_position += 100

    return (new_position == 0), new_position


for rotation in rotations_list:
    result = is_dial_position_zero(dial_start_position, rotation)
    if result[0] is True:
        dial_at_zero_count += 1
    dial_start_position = result[1]

