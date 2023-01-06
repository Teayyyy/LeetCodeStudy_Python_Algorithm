class WordSearch:
    def exist(self, board: [[str]], word: str) -> bool:
        # TODO: Problem: this method finishes without considering the visited character
        # get the first character in word, maybe there is a lot
        char = word[0]
        xs, ys = [], []

        # the DFS algorithm
        # cur_char: the index of current char;  pos: the position, x and y
        def DFS(cur_char: int, pos: [int, int]) -> bool:
            # Escape from recursion
            if board[pos[0]][pos[1]] != word[cur_char]:
                return False
            # Four directions, UP, DOWN, LEFT, RIGHT
            if board[pos[0]][pos[1]] == word[cur_char]:
                # means reach the end, return True
                if cur_char == len(word) - 1:
                    return True
                else:
                    directions = []
                    if pos[0] - 1 >= 0:
                        directions.append([pos[0] - 1, pos[1]])
                    if pos[0] + 1 <= len(board) - 1:
                        directions.append([pos[0] + 1, pos[1]])
                    if pos[1] - 1 >= 0:
                        directions.append([pos[0], pos[1] - 1])
                    if pos[1] + 1 <= len(board[0]) - 1:
                        directions.append([pos[0], pos[1] + 1])
                    return any(DFS(cur_char + 1, [direc[0], direc[1]]) for direc in directions)
            pass

        for i in range(len(board)):
            if char in board[i]:
                for j in range(len(board[i])):
                    if board[i][j] == char:
                        xs.append(i)
                        ys.append(j)
        # for i in range(len(xs)):
        #     print('now:', xs[i], ys[i])
        #     DFS(0, [xs[i], ys[i]])
        return any(DFS(0, [xs[i], ys[i]]) for i in range(len(xs)))

    def exist_2(self, board: [[str]], word: str) -> bool:
        # make a array to save which character has been visited:
        visited = []
        char = word[0]
        xs, ys = [], []

        # DFS:
        # cur_char: the index of current char;  pos: the position, x and y, visited: which character has been visited
        def DFS(cur_char: int, pos: [int, int], visited: [[int, int]]):
            if board[pos[0]][pos[1]] != word[cur_char]:
                return False
            else:
                if cur_char == len(word) - 1:
                    return True
                else:
                    visited.append(pos)
                    directions = []
                    if pos[0] - 1 >= 0 and [pos[0] - 1, pos[1]] not in visited:
                        directions.append([pos[0] - 1, pos[1]])
                    if pos[0] + 1 <= len(board) - 1 and [pos[0] + 1, pos[1]] not in visited:
                        directions.append([pos[0] + 1, pos[1]])
                    if pos[1] - 1 >= 0 and [pos[0], pos[1] - 1] not in visited:
                        directions.append([pos[0], pos[1] - 1])
                    if pos[1] + 1 <= len(board[0]) - 1 and [pos[0], pos[1] + 1] not in visited:
                        directions.append([pos[0], pos[1] + 1])
                    return any(DFS(cur_char + 1, [direc[0], direc[1]], visited[:]) for direc in directions)

            pass

        for i in range(len(board)):
            if char in board[i]:
                for j in range(len(board[i])):
                    if board[i][j] == char:
                        xs.append(i)
                        ys.append(j)

        return any(DFS(0, [xs[i], ys[i]], visited[:]) for i in range(len(xs)))

    def exist_3(self, board: [[str]], word: str) -> bool:
        m, n = len(board), len(board[0])  # m rows, n cols
        print(m, n)
        # get the same array as visited
        visited = []
        for i in range(m):
            visited.append([False for j in range(n)])
        # the core DFS
        def search_DFS(t_i: int, t_j: int, count: int) -> bool:
            # if visited do nothing
            print("t_i: {}, t_j: {}".format(t_i, t_j))
            if visited[t_i][t_j]:
                return False
            elif board[t_i][t_j] != word[count]:
                return False
            else:  # board[i][j] == word[count]
                # if all characters in word shows up
                if count == len(word) - 1:
                    return True

                visited[t_i][t_j] = True
                count += 1
                # begin DFS, up down left right
                directions = []
                if t_i - 1 >= 0:
                    directions.append([t_i - 1, t_j])
                if t_i + 1 <= m - 1:
                    directions.append([t_i + 1, t_j])
                if t_j - 1 >= 0:
                    directions.append([t_i, t_j - 1])
                if t_j + 1 <= n - 1:
                    directions.append([t_i, t_j + 1])
                result = any(search_DFS(direction[0], direction[1], count) for direction in directions)
                visited[t_i][t_j] = False
                return result
            pass

        # know which position in board contains the first character in word
        queue = []
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    queue.append([i, j])
        print(queue)
        # visited the whole queue, using DFS which the details will be evaluated in.
        return any(search_DFS(single[0], single[1], count=0) for single in queue)
        pass


w = WordSearch()
print(w.exist_3(board=[["C","A","A"],["A","A","A"],["B","C","D"]], word="AAB"))
