a, b = map(int, input().split())
for i in range(a):
    for j in range(1, b+1):
        if (i+j) % 2 != 0:
            print('.', end=' ')
        else:
            print('*', end=' ')
    print()