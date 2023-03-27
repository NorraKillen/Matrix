n = int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]
matrix_numbers1 = []
for i in range(n):
    for j in range(n):
        matrix_numbers1.append(matrix[i][j])
matrix_sum = [sum(matrix[i]) for i in range(n)]
matrix_numbers = [number for number in range(1, n**2+1)]

if set(matrix_numbers) == set(matrix_numbers1):
    if matrix_sum.count(matrix_sum[0]) == n:
        matrix_1 = [[matrix[i][j] for i in range(n)] for j in range(n)]
        matrix_sum = [sum(matrix_1[i]) for i in range(n)]
        if matrix_sum.count(matrix_sum[0]) == n:
            matrix_1 = sum([matrix[i][i] for i in range(n)])
            matrix_2 = sum([matrix[i][-i-1] for i in range(n)])
            if matrix_1 == matrix_2:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')