xy = input()
y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])
list = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        a = (x - i) * (y - j)
        if a == 2 or a == -2:
            list[j][i] = '*'
        else:
            list[j][i] = '.'
list[y][x] = 'N'
for i in range(8):
    print(*list[i])