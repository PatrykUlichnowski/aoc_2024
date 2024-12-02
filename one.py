input = open("aoc2024\day one\data.txt")

left_side = []
right_side = []

for line in input:
    split_line = line.split()
    left_side.append(split_line[0])
    right_side.append(split_line[1])

for i in range(0,len(left_side)):
    left_side[i] = int(left_side[i])
    right_side[i] = int(right_side[i])

left_side_sorted = sorted(left_side)
right_side_sorted = sorted(right_side)
#part1
sum = 0
for i in range(0, len(left_side_sorted)):
    sum += abs(left_side_sorted[i] - right_side_sorted[i])
print(sum) 

#part2
part2 = 0
for i in range(len(left_side_sorted)):
    if i == 0 or left_side_sorted[i] != left_side_sorted[i-1]:
        how_often = 0
        for j in range(len(right_side_sorted)):
            if left_side_sorted[i] == right_side_sorted[j]:
                how_often += 1
        part2 += left_side_sorted[i] * how_often
print(part2)