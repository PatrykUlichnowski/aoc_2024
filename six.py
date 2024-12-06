def print_map():
    for line in map:
        print(line)

data_file = open("aoc2024\day six\data.txt") #reading the data
map = []
for line in data_file:
    map.append(list(line.strip()))
data_file.close()

print_map() #initial state
found = False
index_y = 0
index_x = 0
while(not found):
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == "^":
                index_x = i
                index_y = j
                found = True
print("starting position of '^': ",index_x, index_y)
the_end = False
while not the_end:
    if map[index_x][index_y] == "^": #going up
        if index_x - 1 < 0: #the end of the map
            map[index_x][index_y] = "X"
            the_end = True
        elif map[index_x - 1][index_y] != "#": #if not blocked
            map[index_x][index_y] = "X"
            map[index_x -1 ][index_y] = "^"
            index_x -= 1
        else:  #if blocked
            map[index_x][index_y] = "X"
            map[index_x][index_y + 1] = ">"
            index_y += 1
    if map[index_x][index_y] == ">": #going right
        if index_y + 1 == len(map[index_x]): #the end of the map
            map[index_x][index_y] = "X"
            the_end = True
        elif map[index_x][index_y + 1] != "#": #if not blocked
            map[index_x][index_y] = "X"
            map[index_x][index_y + 1] = ">"
            index_y += 1
        else:  #if blocked
            map[index_x][index_y] = "X"
            map[index_x + 1][index_y] = "v"
            index_x += 1
    if map[index_x][index_y] == "v": #going down
        if index_x + 1 == len(map): #the end of the map
            map[index_x][index_y] = "X"
            the_end = True
        elif map[index_x + 1][index_y] != "#": #if not blocked
            map[index_x][index_y] = "X"
            map[index_x + 1][index_y] = "v"
            index_x += 1
        else:  #if blocked
            map[index_x][index_y] = "X"
            map[index_x][index_y - 1] = "<"
            index_y -= 1
    if map[index_x][index_y] == "<": #going left
        if index_y - 1 < 0: #the end of the map
            map[index_x][index_y] = "X"
            the_end = True
        elif map[index_x][index_y - 1] != "#": #if not blocked
            map[index_x][index_y] = "X"
            map[index_x][index_y - 1] = "<"
            index_y -= 1
        else:  #if blocked
            map[index_x][index_y] = "X"
            map[index_x - 1][index_y] = "^"
            index_x -= 1
    # print_map() #printing step by step
    # print('\n')

answer = 0
for line in map:
    for char in line:
        if char == "X":
            answer += 1
print("answer ", answer)
#v^><