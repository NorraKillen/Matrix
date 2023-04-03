a, b = map(int, input().split())
lst = [[int(i) for i in input().split()] for j in range(a)]
input()
lst1 = [[int(i) for i in input().split()] for j in range(a)]
lstsum = [[0]*b for i in range(a)]
for i in range(a):
    for j in range(b):
        lstsum[i][j] = lst[i][j] + lst1[i][j]
for i in lstsum:
    print(*i)