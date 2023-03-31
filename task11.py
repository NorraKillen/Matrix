a = int(input())
l = [[0 for i in range(a)]for j in range(a)]
for i in range(a):
    for j in range(a):
        if i == j or i == a - j - 1 or (i < j and i < a - j-1) or (i > j and i > a - j-1):
            l[i][j] = 1
for i in l:
    print(*i)