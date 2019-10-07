# Matrix Multiplication

row1 = int(input())
column1 = int(input())

matrix1 = [[int(input()) for y1 in range(column1)]for x1 in range(row1)]

matrix2 = [[int(input()) for y2 in range(column1)]for x2 in range(row1)]



print("Matrix 1")
print_matrix1 = [[print(matrix1[x1][y1]) for y1 in range(column1)]for x1 in range(row1)]

print("Matrix2")
print_matrix2 = [[print(matrix2[x2][y2]) for y2 in range(column1)]for x2 in range(row1)]

print("Multiplied Matrix")
Mul_matrix = [[print(matrix1[x1][y1] * matrix2[x1][y1]) for y1 in range(column1)]for x1 in range(row1)]


