a = int(input())
list = []
for i in range(a):
    list.append(input().split())
for i in range(a):
    for j in range(a):
        print(list[a - j - 1][i], end=' ')
    print()