with open('day1_input.txt', 'r') as input_file:
    rotations_list = [line.replace('\n', '') for line in input_file.readlines()]

print(rotations_list)

dial_start_position = 50
dial_at_zero_count = 0


def is_dial_position_zero(starting_position, dial_rotation):
    rotation_direction = dial_rotation[0]
    rotation_distance = int(dial_rotation[1:])
    while rotation_distance > 99:
        rotation_distance -= 100

    if rotation_direction == 'L':
        rotation_distance = -1 * rotation_distance

    new_position = starting_position + rotation_distance

    if new_position > 99:
        new_position -= 100
    elif new_position < 0:
        new_position += 100

    # if rotation_direction == 'R':  # how can I change this loop to remove repetition?
    #     new_position = starting_position + rotation_distance
    #     if new_position > 99:
    #         new_position -= 100
    #     elif new_position < 0:
    #         new_position += 100
    # else:
    #     new_position = starting_position - rotation_distance
    #     if new_position > 99:
    #         new_position -= 100
    #     elif new_position < 0:
    #         new_position += 100

    return (new_position == 0), new_position


for rotation in rotations_list:
    result = is_dial_position_zero(dial_start_position, rotation)
    if result[0] is True:
        dial_at_zero_count += 1
    dial_start_position = result[1]

print(f'The password is {dial_at_zero_count}!')
