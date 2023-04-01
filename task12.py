a, b = map(int, input().split())
for i in range(a):
    for j in range(b):
        print((i + j) % b + 1, end=' ')
    print()