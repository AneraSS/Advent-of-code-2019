#https://adventofcode.com/2019/day/1

with open ('input.txt') as file_object:
    major_sum = 0
    for line in file_object:
        divided_number = int(line)//3 # takes the first digit
        rounded_up = int(round(divided_number,0))-2
        if (int(rounded_up)//3 == 0):
            minor_sum = 0
        elif (int(rounded_up)//3 != 0):
            minor_sum = 0
            minor_sum += rounded_up
            while (int(rounded_up)//3 != 0) and int(rounded_up) > 0:
                rounded_up = (int(rounded_up)//3) - 2
                if rounded_up > 0:
                    minor_sum +=rounded_up
                else:
                    break
        major_sum += minor_sum
        print(f"Status of major sum: minor sum: {minor_sum} => major sum: {major_sum}")
print(f" Major sum: {major_sum}")

# solved: 4974073