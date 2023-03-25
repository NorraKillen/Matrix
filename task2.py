a = int(input())
k = []
for i in range(a):
    k.append(input().split())
for i in k[::-1]:
    print(*i)
