a, b = map(int, input().split())
v = [i for i in range(1, a*b+1)]
for i in range(a):
    for j in range(b):
        print( 1 + i + j * a , end=' ')
    print()