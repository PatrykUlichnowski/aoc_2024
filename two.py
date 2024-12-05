data_file = open("aoc2024\day two\data.txt")
tab = []

for row in data_file:
    tab.append(row.split())

for i in range(len(tab)):
    for j in range(len(tab[i])):
        tab[i][j] = int(tab[i][j])



save_sum = 0
for i in range(len(tab)):
    good = True
    inc = False
    dec = False
    for j in range(1, len(tab[i])):
        if tab[i][j] > tab[i][j - 1]:
            if not 1 <= tab[i][j] - tab[i][j-1] <=3:
                good = False
            inc = True
        elif tab[i][j] < tab[i][j - 1]:
            if not -3 <= tab[i][j] - tab[i][j-1] <= -1:
                good = False
            dec = True
    if inc and good and dec == False:
        save_sum += 1
    if dec and good and inc == False:
        save_sum += 1

# for row in tab:
#     inc = row[1] > row[0]
#     correct = True
#     if inc:
#         for i in range(1, len(row)):
#             if not 1<= row[i] - row[i-1] <= 3:
#                 correct = False
#         if correct:
#             save_sum += 1
#     else:
#         for i in range(1, len(row)):
#             if not -3 <= row[i] - row[i-1] <= -1:
#                 correct = False
#         if correct:
#             save_sum += 1

print(save_sum) #472