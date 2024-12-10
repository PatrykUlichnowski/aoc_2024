data_file = open("data.txt")
data_map = data_file.readline().strip()
data_file.close()
data = []
base = 0
for i, val in enumerate(data_map):
    if i%2 == 0:
        for i in range(int(val)):
            data.append(base)
        base += 1
    else:
        for i in range(int(val)):
            data.append(".")
        
last = len(data) - 1
for i in range(0, len(data)):
    if data[i] == ".":
        if last >= i:
            while data[last] == ".":
                last -= 1
            data[i] = data[last]
            data[last] = "."
            last -= 1
        else: 
            break

res = 0 
for i, val in enumerate(data):
    if val != ".": 
        res += i * int(val)
    else:
        break
print(res) 