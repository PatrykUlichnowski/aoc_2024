from itertools import product

data_file = open("aoc2024\day seven\data.txt")
data = []
for line in data_file:
    data.append(line.strip())
for i in range(len(data)):
    data[i] = data[i].split()

for i in range(len(data)):
    for j in range(len(data[i])):
        if j == 0:
            data[i][j] = int(data[i][j][:-1])
        data[i][j] = int(data[i][j])

answer = 0

for line in data:
    test_res = line[0]
    print("Searching for ",test_res)
    numbers = line[1:]
    for combo in product("*+|", repeat=len(numbers)-1): #part 2 version, remove the "|" to get part one result
        res = numbers[0]
        for i in range(1, len(numbers)):
            # print("val = ",combo[i-1])
            if combo[i-1] == "+":
                res += numbers[i]
            elif combo[i-1] == "*":
                res *= numbers[i]
            elif combo[i-1] == "|": #part 2
                res = int(f"{res}{numbers[i]}")
        if res == test_res:
            answer += test_res
            break

print(answer)
