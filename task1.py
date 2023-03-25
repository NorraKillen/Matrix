n = int(input())
a = []

for i in range(n):
    a.append(input().split())
for i in range(n):
    for j in range(n):

        a[i][i], a[ - i - 1][i] = a[ - i - 1][i], a[i][i]

for i in range(n):
    print(*a[i])



