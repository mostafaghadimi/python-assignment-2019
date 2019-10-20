a = input()
l = a.split()
m = int(l[0])
n = int(l[1])
matrix = []
for i in range(m):
    row = input().split()
    matrix.append(row)

print(matrix)

count = 0
for i in range(1, m-1):
    for j in range(1, n-1):
        if int(matrix[i][j]) < int(matrix[i][j-1]) and int(matrix[i][j]) < int(matrix[i][j+1]) and int(matrix[i][j]) > int(matrix[i-1][j]) and int(matrix[i][j]) > int(matrix[i+1][j]):
            count += 1
print(count)        