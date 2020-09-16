
def diagonal_difference():
    n = int(input())
    matrix = get_matrix_input(n)
    rightDiagonalSum = find_right_diagonal_sum(matrix)
    leftDiagonalSum = find_left_diagonal_sum(matrix)
    absoluteDiagonalDifference = find_absolute_diagonal_difference(
        leftDiagonalSum,
        rightDiagonalSum
    )
    return  absoluteDiagonalDifference


def get_matrix_input(matrixSize):
     matrix = []
     for i in range(0, matrixSize):
         currValues = list(map(int, input().split()))
         matrix.append(currValues)

     return  matrix

def find_absolute_diagonal_difference(leftSum, rightSum):
    return abs(leftSum - rightSum)

def find_left_diagonal_sum(matrix):
    leftRowIndex = 0
    leftColIndex = 0
    totalDiagonalSum = 0

    while leftRowIndex < len(matrix) and leftColIndex < len(matrix[leftRowIndex]):
         totalDiagonalSum += matrix[leftRowIndex][leftColIndex]
         leftRowIndex += 1
         leftColIndex += 1

    return totalDiagonalSum

def find_right_diagonal_sum(matrix):
    rightRowIndex = 0
    rightColIndex = len(matrix[rightRowIndex]) - 1
    totalRightDiagonalSum = 0

    while rightRowIndex != len(matrix) and rightColIndex != 0:
          totalRightDiagonalSum += matrix[rightRowIndex][rightColIndex]
          rightRowIndex += 1
          rightColIndex -= 1

    totalRightDiagonalSum += matrix[rightRowIndex][rightColIndex]
    return  totalRightDiagonalSum

print(
    diagonal_difference()
)