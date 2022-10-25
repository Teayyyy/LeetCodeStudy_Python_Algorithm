import copy
import numpy as np


class PacificAtlanticWaterFlow:
    def pacific_atlantic(self, heights: [[int]]) -> [[int]]:
        # the height is m x n
        m = len(heights[0]) - 1
        n = len(heights) - 1
        # construct the visit matrix
        # [False, False] means if [i, j] can flow to Pacific and Atlantic
        flows = copy.deepcopy(heights)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                flows[i][j] = [False, False]
                if i == 0:
                    flows[i][j][0] = True
                if i == len(heights[0]) - 1:
                    flows[i][j][1] = True

                if j == 0:
                    flows[i][j][0] = True
                if j == len(heights) - 1:
                    flows[i][j][1] = True

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                # check if it is visited
                # Weather can reach Pacific
                if flows[i][j][0]:
                    # check four directions
                    # up
                    if i - 1 >= 0 and heights[i - 1][j] >= heights[i][j]:
                        flows[i - 1][j][0] = True
                    if i + 1 <= len(heights) - 1 and heights[i + 1][j] >= heights[i][j]:
                        flows[i + 1][j][0] = True
                    if j - 1 >= 0 and heights[i][j - 1] >= heights[i][j]:
                        flows[i][j - 1][0] = True
                    if j + 1 <= len(heights[0]) - 1 and heights[i][j + 1] >= heights[i][j]:
                        flows[i][j + 1][0] = True

                # Weather can reach Atlantic
                if flows[n - i][m - j][1]:
                    if n - i - 1 >= 0 and heights[n - i - 1][m - j] >= heights[n - i][m - j]:
                        flows[n - i - 1][m - j][1] = True
                    if n - i + 1 <= len(heights) - 1 and heights[n - i + 1][m - j] >= heights[n - i][m - j]:
                        flows[n - i + 1][m - j][1] = True
                    if m - j - 1 >= 0 and heights[n - i][m - j - 1] >= heights[n - i][m - j]:
                        flows[n - i][m - j - 1][1] = True
                    if m - j + 1 <= len(heights[0]) - 1 and heights[n - i][m - j + 1] >= heights[n - i][m - j]:
                        flows[n - i][m - j + 1][1] = True

        for i in flows:
            for j in i:
                print(j, "\t", end="")
            print("\n")

        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if flows[i][j][0] and flows[i][j][1]:
                    result.append([i, j])
        return result

    def pacific_atlantic_2(self, heights: [[int]]) -> [[int]]:
        # the height is m x n
        m = len(heights[0]) - 1
        n = len(heights) - 1
        # construct the visit matrix
        # [False, False] means if [i, j] can flow to Pacific and Atlantic
        flows = copy.deepcopy(heights)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                flows[i][j] = [False, False]
                if i == 0:
                    flows[i][j][0] = True
                if i == len(heights[0]) - 1:
                    flows[i][j][1] = True

                if j == 0:
                    flows[i][j][0] = True
                if j == len(heights) - 1:
                    flows[i][j][1] = True

        # The DFS Function
        def DFS(x: int, y: int, side: int):
            # check 4 directions
            if x - 1 >= 0 and heights[x - 1][y] >= heights[x][y] and not flows[x - 1][y][side]:
                flows[x - 1][y][side] = True
                DFS(x - 1, y, side)
            if x + 1 <= len(heights) - 1 and heights[x + 1][y] >= heights[x][y] and not flows[x + 1][y][side]:
                flows[x + 1][y][side] = True
                DFS(x + 1, y, side)
            if y - 1 >= 0 and heights[x][y - 1] >= heights[x][y] and not flows[x][y - 1][side]:
                flows[x][y - 1][side] = True
                DFS(x, y - 1, side)
            if y + 1 <= len(heights[0]) - 1 and heights[x][y + 1] >= heights[x][y] and not flows[x][y + 1][side]:
                flows[x][y + 1][side] = True
                DFS(x, y + 1, side)
            pass

        # using DFS
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                # Pacific
                if flows[i][j][0]:
                    # DFS
                    DFS(i, j, 0)
                    pass
                if flows[n - i][m - j][1]:
                    # DFS
                    DFS(n - i, m - j, 1)
                    pass

        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if flows[i][j][0] and flows[i][j][1]:
                    result.append([i, j])
        return result

    def pacific_atlantic_3(self, heights: [[int]]) -> [[int]]:
        # the height is m x n
        m = len(heights[0]) - 1
        n = len(heights) - 1
        # construct the visit matrix
        # [False, False] means if [i, j] can flow to Pacific and Atlantic
        flows = copy.deepcopy(heights)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                flows[i][j] = [False, False]

        # DFS Algorithm
        def DFS(x, y, side):
            if flows[x][y][side]:
                return
            flows[x][y][side] = True
            # UP
            if x - 1 >= 0 and heights[x - 1][y] >= heights[x][y]:
                DFS(x - 1, y, side)
            # DOWN
            if x + 1 <= len(heights) - 1 and heights[x + 1][y] >= heights[x][y]:
                DFS(x + 1, y, side)
            # LEFT
            if y - 1 >= 0 and heights[x][y - 1] >= heights[x][y]:
                DFS(x, y - 1, side)
            # RIGHT
            if y + 1 <= len(heights[0]) - 1 and heights[x][y + 1] >= heights[x][y]:
                DFS(x, y + 1, side)
            pass

        # Since only four edges will reach two oceans
        for j in range(len(heights[0])):
            # Pacific
            DFS(0, j, 0)
            # Atlantic
            DFS(n, m - j, 1)
            pass

        for i in range(len(heights)):
            # Pacific
            DFS(i, 0, 0)
            # Atlantic
            DFS(n - i, m, 1)
            pass

        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if flows[i][j][0] and flows[i][j][1]:
                    result.append([i, j])
        return result

    def AtlanticPacific(self, heights: [[int]]) -> [[int]]:
        # the height is m x n
        m = len(heights[0]) - 1
        n = len(heights) - 1
        # construct the visit matrix
        # [False, False] means if [i, j] can flow to Pacific and Atlantic
        flows = copy.deepcopy(heights)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                flows[i][j] = [False, False]

        # DFS Algorithm
        def DFS(x, y, side):
            if flows[x][y][side]:
                return
            flows[x][y][side] = True
            # UP
            if x - 1 >= 0 and heights[x - 1][y] >= heights[x][y]:
                DFS(x - 1, y, side)
            # DOWN
            if x + 1 <= len(heights) - 1 and heights[x + 1][y] >= heights[x][y]:
                DFS(x + 1, y, side)
            # LEFT
            if y - 1 >= 0 and heights[x][y - 1] >= heights[x][y]:
                DFS(x, y - 1, side)
            # RIGHT
            if y + 1 <= len(heights[0]) - 1 and heights[x][y + 1] >= heights[x][y]:
                DFS(x, y + 1, side)
            pass

        # Since only four edges will reach two oceans
        for j in range(len(heights[0])):
            # Pacific
            DFS(0, j, 0)
            # Atlantic
            DFS(n, m - j, 1)
            pass

        for i in range(len(heights)):
            # Pacific
            DFS(i, 0, 0)
            # Atlantic
            DFS(n - i, m, 1)
            pass

        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if flows[i][j][0] and flows[i][j][1]:
                    result.append([i, j])
        return result



p = PacificAtlanticWaterFlow()
# print(p.pacific_atlantic_3([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
# print(p.pacific_atlantic_2([[2, 1], [1, 2]]))
print(p.AtlanticPacific([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
