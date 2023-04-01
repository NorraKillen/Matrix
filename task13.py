a, b = map(int, input().split())
k = [i for i in range(1, a*b+1)]
for i in range(a):
    if i % 2 != 0:
        print(*k[b-1::-1])
    else:
        print(*k[:b])
    del k[:b]
