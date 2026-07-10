def main(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n - i - 1):
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
            matrix[i][n - j - 1], matrix[n - i - 1][n - j - 1] = matrix[n - i - 1][n - j - 1], matrix[i][n - j - 1]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(*row)

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = main(matrix)
    print_matrix(matrix)
