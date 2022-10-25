class Solution:
    memorization = []

    def max_area(self, grid: [[int]]) -> int:
        # construct the memory-matrix
        temp = []
        for i in range(len(grid[0])):
            temp.append(0)
        for i in range(len(grid)):
            Solution.memorization.append(temp.copy())

        # Traverse the whole grid, if the current element has been visited(shows 1 in memorization-matrix at the same
        # position, skip it
        i, j, size = 0, 0, 0
        while True:
            if grid[i][j] == 1 and Solution.memorization[i][j] != 1:
                Solution.memorization[i][j] = 1
                # size = max(self.deep_first_traverse_modified(grid, i, j, 0), size)
                size = max(self.deep_first_traverse_remaster(grid, i, j), size)
                print('-' * 30)
            j += 1
            if j > len(grid[0]) - 1:
                j = 0
                i += 1
            if i > len(grid) - 1:
                Solution.memorization = []
                return size
            pass

    def deep_first_traverse_modified(self, grid: [[int]], i: int, j: int, last_move: int) -> int:
        '''
        Shows how big the island is, using DFS algorithm, if this piece of island has been visited, skip to the next
        Only the up-down-left-right side of the grid should include in the size of this island
        You need to check the last-time movement, and do the proper check
        :param grid: the whole area
        :param i: vertical index
        :param j: horizontal index
        :param last_move: the last movement, if UP (LEFT, RIGHT, DOWN), LEFT (UP, DOWN, RIGHT)， vice versa
                0: UP, 1: DOWN, 2:LEFT, 3: RIGHT
        :return: the size of the island
        '''
        print("i: {0}, j: {1}".format(i, j))
        size = 0

        # some re-used codes: up, down, left, right
        def m_up(size: int) -> int:
            # print(size)
            if i - 1 >= 0 and grid[i - 1][j] == 1 and Solution.memorization[i - 1][j] == 0:
                Solution.memorization[i - 1][j] = 1
                # move to i - 1, means the original is DOWN
                size += self.deep_first_traverse_modified(grid, i - 1, j, 1)
            return size

        def m_down(size: int) -> int:
            if i + 1 <= len(grid) - 1 and grid[i + 1][j] == 1 and Solution.memorization[i + 1][j] == 0:
                Solution.memorization[i + 1][j] = 1
                size += self.deep_first_traverse_modified(grid, i + 1, j, 0)
            return size

        def m_left(size: int) -> int:
            if j - 1 >= 0 and grid[i][j - 1] == 1 and Solution.memorization[i][j - 1] == 0:
                Solution.memorization[i][j - 1] = 1
                size += self.deep_first_traverse_modified(grid, i, j - 1, 3)
            return size

        def m_right(size: int) -> int:
            if j + 1 <= len(grid[0]) - 1 and grid[i][j + 1] == 1 and Solution.memorization[i][j + 1] == 0:
                Solution.memorization[i][j + 1] = 1
                size += self.deep_first_traverse_modified(grid, i, j + 1, 2)
            return size

        if last_move == 0:
            # TODO: DOWN, LEFT, RIGHT
            size = m_down(size)
            size = m_left(size)
            size = m_right(size)
            pass
        elif last_move == 1:
            # TODO: UP, LEFT, RIGHT
            size = m_up(size)
            size = m_left(size)
            size = m_right(size)
            pass
        elif last_move == 2:
            # TODO: UP, DOWN, RIGHT
            size = m_up(size)
            size = m_down(size)
            size = m_right(size)
            pass
        elif last_move == 3:
            # TODO: UP, DOWN, LEFT
            size = m_up(size)
            size = m_down(size)
            size = m_left(size)
            pass
        size += 1
        return size

    def deep_first_traverse(self, grid: [[int]], i: int, j: int) -> int:
        '''
        Shows how big the island is, using DFS algorithm, if this piece of island has been visited, skip to the next
        Only the up-down-left-right side of the grid should include in the size of this island
        :param grid: the whole area
        :param i: vertical index
        :param j: horizontal index
        :return: the size of the island
        '''
        print("i: {0}, j: {1}".format(i, j))
        # get the size recursively
        size = 0
        # traverse sequence: UP RIGHT DOWN
        if i - 1 >= 0 and grid[i - 1][j] == 1 and Solution.memorization[i - 1][j] == 0:
            Solution.memorization[i - 1][j] = 1
            size += self.deep_first_traverse(grid, i - 1, j)
        if j + 1 < len(grid[0]) - 1 and grid[i][j + 1] == 1 and Solution.memorization[i][j + 1] == 0:
            Solution.memorization[i][j + 1] = 1
            size += self.deep_first_traverse(grid, i, j + 1)
        if i + 1 < len(grid) and grid[i + 1][j] == 1 and Solution.memorization[i + 1][j] == 0:
            Solution.memorization[i + 1][j] = 1
            size += self.deep_first_traverse(grid, i + 1, j)
        # count on this piece
        size += 1
        # Solution.memorization[i][j] = 1
        return size

    def deep_first_traverse_remaster(self, grid: [[int]], i: int, j: int) -> int:
        # TODO: Do the optimize version of this, see leetcode, using DFS, ignore direction(up, down, left, right) judge
        # TODO: Unify it to speed up the process
        print("i: {0}, j: {1}".format(i, j))
        size = 0
        if i - 1 >= 0 and grid[i - 1][j] == 1 and Solution.memorization[i - 1][j] == 0:
            Solution.memorization[i - 1][j] = 1
            size += self.deep_first_traverse_remaster(grid, i - 1, j)
        if i + 1 <= len(grid) - 1 and grid[i + 1][j] == 1 and Solution.memorization[i + 1][j] == 0:
            Solution.memorization[i + 1][j] = 1
            size += self.deep_first_traverse_remaster(grid, i + 1, j)
        if j - 1 >= 0 and grid[i][j - 1] == 1 and Solution.memorization[i][j - 1] == 0:
            Solution.memorization[i][j - 1] = 1
            size += self.deep_first_traverse_remaster(grid, i, j - 1)
        if j + 1 <= len(grid[0]) - 1 and grid[i][j + 1] == 1 and Solution.memorization[i][j + 1] == 0:
            Solution.memorization[i][j + 1] = 1
            size += self.deep_first_traverse_remaster(grid, i, j + 1)

        size += 1
        return size


m = Solution()
# print(m.max_area([[1, 1]]))
print(m.max_area([[1], [1]]))
