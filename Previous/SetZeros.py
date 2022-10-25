class SetZeros:
    def set_zeros(self, matrix: [[int]]) -> None:
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append([i, j])
        for zero in zeros:
            matrix[zero[0]] = [0 for i in range(len(matrix[0]))]
            for i in range(len(matrix)):
                matrix[i][zero[1]] *= 0

        for i in matrix:
            print(i)


s = SetZeros()

matrix_1 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

s.set_zeros(matrix_1)
