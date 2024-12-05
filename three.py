import re

file = open("aoc2024\day three\data.txt")
data = file.readline()
regex_result = re.findall("mul\([0-9]+,[0-9]+\)", data)
print(regex_result)
sum = 0
for operation in regex_result:
    operation = operation.strip("mul()")
    operation = operation.split(",")
    sum += int(operation[0]) * int(operation[1])
print(sum)