#https://adventofcode.com/2019/day/1

with open ('test.txt') as file_object:
    major_sum = 0
    for line in file_object:
        divided_number = int(line) // 3  # takes the first digit
        rounded_up = int(round(divided_number, 0))
        subtracted_number = rounded_up - 2
        number = subtracted_number
        print(rounded_up)
        if (number//3) != 0:
            while (number//3) != 0:
                minor_sum = number
                print(f"Entering loop, status of minor sum: {minor_sum}")
                new_number_rounded = int(round(divided_number, 0))
                new_number_subtracted = new_number_rounded - 2
                print (f"Number obtained: {new_number_subtracted}")
            number = new_number_subtracted
            minor_sum += new_number_subtracted

        major_sum += minor_sum

print((major_sum))