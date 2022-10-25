class Solutionss:
    def matrixReshape(self, mat: [[int]], r: int, c: int) -> [[int]]:
        # 检查数据的大小是否合理
        if len(mat) * len(mat[0]) != r * c:
            return mat
        else:
            lines = []
            for row in mat:
                for item in row:
                    lines.append(item)
            print(lines)
            final = []
            for i in range(r):
                temp = []
                for j in range(c):
                    print(r * i + j)
                    temp.append(lines[r * i + j])
                final.append(temp)

        return final


s = Solutionss()
s.matrixReshape([[1, 2], [3, 4]], 1, 4)
