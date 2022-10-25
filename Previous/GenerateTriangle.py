class GenerateTriangle:
    def generate(self, numRows: int) -> [[int]]:
        triangle = []
        count = 0
        for row in range(1, numRows + 1):
            layer = []
            for i in range(row):
                if i == 0 or i == row - 1:
                    layer.append(1)
                    count += 1
                else:
                    layer.append(triangle[row - 2][i] + triangle[row - 2][i - 1])
                    count += 1
                print("count: {0}".format(count))
            triangle.append(layer)
        return triangle

g = GenerateTriangle()
generated = g.generate(10)
print(generated, sep="\n")