#https://adventofcode.com/2019/day/1

with open ('test.txt') as file_object:
    final_sum = 0
    for line in file_object:
        divided_number = int(line)//3 # takes the first digit
        rounded_up = int(round(divided_number,0))-2
        minor_sum = 0



        while int(rounded_up)//3 != 0:
            rounded_up = (int(rounded_up)//3)-2
            minor_sum += rounded_up
        print(rounded_up)


