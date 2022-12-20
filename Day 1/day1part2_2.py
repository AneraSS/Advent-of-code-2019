#https://adventofcode.com/2019/day/1

with open ('test.txt') as file_object:
    major_sum = 0
    for line in file_object:
        divided_number = int(line)//3 # takes the first digit
        rounded_up = int(round(divided_number,0))-2
        minor_sum = 0
        if (int(rounded_up)//3 == 0):
            minor_sum = 0
            print(minor_sum)
            major_sum += major_sum
        elif (int(rounded_up)//3 != 0):
            minor_sum = 0
            minor_sum += rounded_up
            while (int(rounded_up)//3 != 0):
                print(f"Status of minor sum: {minor_sum}")
                rounded_up = (int(rounded_up)//3) - 2
                print(f"New number: {rounded_up}")
                print(f"Sum: {minor_sum}")
                minor_sum+=rounded_up
            print(f"Final minor sum: {minor_sum}")
        major_sum += minor_sum
print(f" Major sum: {major_sum}")

# ne radi na 1969, 20, 19,