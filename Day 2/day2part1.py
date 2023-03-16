# https://adventofcode.com/2019/day/2

with open('input.txt') as file:
    contents = file.read()
    numbers_str = contents.split(",") # convert  into list of string numbers separated by comma

    numbers_int = []
    for number in numbers_str:
        numbers_int.append(int(number)) # convert into list of integers separated by comma

    instruction_list = numbers_int     # list of numbers (integers)
    current_instruction_index = 0
    instruction_list[1] = 12
    instruction_list[2] = 2

    while current_instruction_index < len(instruction_list):
        if instruction_list[current_instruction_index] == 1:
            position_input_one = instruction_list[current_instruction_index+1]
            position_input_two = instruction_list[current_instruction_index+2]
            position_output = instruction_list[current_instruction_index+3]

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

print (instruction_list[0])

# answer: 4930687