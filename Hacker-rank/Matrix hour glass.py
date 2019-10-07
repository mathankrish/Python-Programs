#arr = [list(map(int, input().split())) for _ in range(6)]
#
# total = 0
# max_total = -1
#
# for i in range(len(arr) - 2):
#     for j in range(len(arr) - 2):
#
#         total = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
#         max_total = max(max_total, total)
#
# print(max_total)

def hourclass(arr, i, j):

    return arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

arr = [list(map(int, input().split())) for _ in range(6)]

max = max([hourclass(arr, i, j) for j in range(len(arr) - 2) for i in range(len(arr) - 2)])

print(max)