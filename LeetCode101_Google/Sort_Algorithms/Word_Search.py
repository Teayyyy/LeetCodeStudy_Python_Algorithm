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

w = WordSearch()
print(w.exist_2(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
