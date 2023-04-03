a = int(input())
lst = [[int(i) for i in input().split()] for j in range(a)]
lst1 = lst
b = int(input())

for _ in range(b-1):
    lstsum = [[0]*a for i in range(a)]
    for i in range(a):
        for j in range(a):
            for o in range(a):
                lstsum[i][j] += lst[i][o]*lst1[o][j]
    lst1 = lstsum

for i in lstsum:
    print(*i)
