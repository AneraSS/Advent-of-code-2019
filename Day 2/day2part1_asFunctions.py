# https://adventofcode.com/2019/day/2

def create_integer_list_from_string_list (contents):
    """From input list of sting create list of integers"""
    numbers_str = contents.split(",")  # convert  into list of string numbers separated by comma
    numbers_int = []
    for number in numbers_str:
        numbers_int.append(int(number))  # convert into list of integers separated by comma
    return numbers_int


def execute_instruction(position_start_instruction, intcode_program):
    opcode = intcode_program[position_start_instruction]
    position_one = intcode_program[position_start_instruction+1]
    position_two = intcode_program[position_start_instruction+2]
    outcome_position = intcode_program[position_start_instruction+3]

    if opcode ==1:
        intcode_program[outcome_position] = intcode_program[position_one] + intcode_program[position_two]
    if opcode == 2:
        intcode_program[outcome_position] = intcode_program[position_one] * intcode_program[position_two]

with open('input.txt') as file:
    intcode_program = create_integer_list_from_string_list(file.read())

    current_instruction_index = 0
    intcode_program[1] = 12
    intcode_program[2] = 2

    while current_instruction_index < len(intcode_program):
        if intcode_program[current_instruction_index] == 99:
            break

        execute_instruction(current_instruction_index, intcode_program)

        current_instruction_index += 4

print (intcode_program[0])

# answer: 4930687