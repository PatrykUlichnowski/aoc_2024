data_file = open("aoc2024\day four\data.txt") 
lines = []
for line in data_file:
    lines.append(line.strip())

lines_len = len(lines)
row_len = len(lines[0])

# Generate tuple of all directions
direction = []
for direction_x in range(-1, 2):
    for direction_y in range(-1, 2):
        if direction_x != 0 or direction_y != 0:
            direction.append((direction_x, direction_y))

# direction = [(-1, -1), (-1, 0), (-1, 1),
#               (0, -1),           (0, 1),
#               (1, -1), (1, 0), (1, 1)]

def has_xmas(i, j, direction_tuple):
    direction_x, direction_y = direction_tuple
    for index, letter in enumerate("XMAS"):
        ii = i + index * direction_x
        jj = j + index * direction_y
        if not (0 <= ii < lines_len and 0 <= jj < row_len):
            return False
        if lines[ii][jj] != letter:
            return False
    return True

sum = 0
for i in range(lines_len):
    for j in range(row_len):
        for tuple in direction:
            sum += has_xmas(i, j, tuple)

print(sum)