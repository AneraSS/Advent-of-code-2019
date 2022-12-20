#https://adventofcode.com/2019/day/1

with open ('input.txt') as file_object:
    final_sum = 0
    for line in file_object:
        divided_number = int(line)//3 # takes the first digit
        rounded_up = int(round(divided_number,0))
        subtracted_number = rounded_up-2
        final_sum+=subtracted_number
print(final_sum)

# solved (3317970)


