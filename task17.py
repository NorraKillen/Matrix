a, b = map(int, input().split())
lst = [[int(i) for i in input().split()] for j in range(a)]
input()
c, v = map(int, input().split())
lst1 = [[int(i) for i in input().split()] for j in range(c)]
lstsum = [[0]*v for i in range(a)]

for i in range(a):
    for j in range(v):
        for o in range(c):
            lstsum[i][j] += lst[i][o]*lst1[o][j]
for i in lstsum:
    print(*i)