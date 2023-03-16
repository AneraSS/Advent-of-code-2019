# https://adventofcode.com/2019/day/2#part2

def execute_program (noun, verb, instruction_list):
    instruction_list = instruction_list[::] # resetting the list, copy of itself, so it won't change initial list
    instruction_list[1] = noun
    instruction_list[2] = verb

    current_instruction_index = 0

    while current_instruction_index < len(instruction_list):
        if instruction_list[current_instruction_index] == 1:
            position_input_one = instruction_list[current_instruction_index + 1]
            position_input_two = instruction_list[current_instruction_index + 2]
            position_output = instruction_list[current_instruction_index + 3]

            # making changes to the list
            value_one = instruction_list[position_input_one]
            value_two = instruction_list[position_input_two]
            output_value = (value_one + value_two)
            instruction_list[position_output] = output_value

        if instruction_list[current_instruction_index] == 2:
            position_input_one = instruction_list[current_instruction_index + 1]
            position_input_two = instruction_list[current_instruction_index + 2]
            position_output = instruction_list[current_instruction_index + 3]

            # making changes to the list
            value_one = instruction_list[position_input_one]
            value_two = instruction_list[position_input_two]
            output_value = (value_one * value_two)
            instruction_list[position_output] = output_value

        if instruction_list[current_instruction_index] == 99:
            break

        current_instruction_index += 4

    return instruction_list[0]

with open('input.txt') as file:
    contents = file.read()
    numbers_str = contents.split(",") # convert  into list of string numbers separated by comma

    numbers_int = []
    for number in numbers_str:
        numbers_int.append(int(number)) # convert into list of integers separated by comma

    instruction_list = numbers_int     # list of numbers (integers)

    for noun in range (0,99):
        for verb in range (0,99):
            result = execute_program(noun,verb,instruction_list)
            if result == 19690720:
                print (noun, verb, 100*noun + verb)

# answer: 5335