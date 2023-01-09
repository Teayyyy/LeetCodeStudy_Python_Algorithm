class N_Queens:
    def solveNQueens(self, n: int) -> [[str]]:
        # show which line is or is not visited
        all_row = [False for i in range(n)]
        print("All Rows: \n", all_row)
        # make board
        board = []
        for i in range(n):
            board.append(['.' for j in range(n)])
        print("Board: ", end="\n")
        for i in board:
            print(i)

        def DFS(t_board: [[str]], t_all_row: [bool], last_ind: [int, int]) -> bool:

            pass

        # Each element in Row 1
        for i in range(n):
            DFS(board[:], all_row[:], last_ind=[0, i])
        pass

    def solveNQueens_2(self, n: int) -> [[str]]:
        # show which line is or is not visited
        all_rows = [False for i in range(n)]
        all_cols = [False for i in range(n)]
        # make board, and final answers
        board = []
        for i in range(n):
            board.append(['.' for j in range(n)])
        for i in board:
            print(i)
        answers = []  # to save all the solutions

        def Queen_DFS(t_board: [[str]], t_all_rows: [bool], t_all_cols: [bool], ind: [int, int]) -> bool:
            print("ind: ", ind)
            # check if there's a queen, or if this position will be attacked
            if t_board[ind[0]][ind[1]] == 'Q':
                return False
            # up and down threat
            # if 'Q' in t_board[:][ind[1]] or 'Q' in t_board[ind[0]][:]:
            #     return False
            if 'Q' in t_board[ind[0]]:
                return False
            for x in t_board:
                if x[ind[1]] == 'Q':
                    return False
            # oblique threat
            # case1: \ direction
            sub = min(ind)
            i, j = ind[0] - sub, ind[1] - sub
            while i <= n - 1 and j <= n - 1:
                if t_board[i][j] == 'Q':
                    return False
                i += 1
                j += 1
            # case2: / direction
            sub = n - ind[0] - 1
            i = ind[0] + sub
            j = ind[1] - sub
            while i >= 0 and j <= n - 1:
                if t_board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            # if run to this point, all 8 directions is out of threat, can place a Queen
            t_board[ind[0]][ind[1]] = "Q"
            t_all_rows[ind[0]] = True
            if all(t_all_rows) or all(t_all_cols):
                answers.append(t_board[:])
                return True
            # if i - 1 >= 0 and j - 2 >= 0:
            #     Queen_DFS(t_board=t_board[:], t_all_rows=t_all_rows[:], ind=[i - 1, j - 2])
            # if i - 2 >= 0 and j + 1 <= n - 1:
            #     Queen_DFS(t_board=t_board[:], t_all_rows=t_all_rows[:], ind=[i - 2, j + 1])
            # if i + 2 <= n - 1 and j - 1 >= 0:
            #     Queen_DFS(t_board=t_board[:], t_all_rows=t_all_rows[:], ind=[i + 2, j - 1])
            # if i + 1 <= n - 1 and j + 2 <= n + 1:
            #     Queen_DFS(t_board=t_board[:], t_all_rows=t_all_rows[:], ind=[i + 1, j + 2])
            pass
            # find four directions to do next iterations
            if ind[0] - 1 >= 0 and ind[1] - 2 >= 0:
                Queen_DFS(t_board=t_board[:][:], t_all_rows=t_all_rows[:], t_all_cols=t_all_cols[:], ind=[ind[0] - 1, ind[1] - 2])
            if ind[0] - 2 >= 0 and ind[1] + 1 <= n - 1:
                Queen_DFS(t_board=t_board[:][:], t_all_rows=t_all_rows[:], t_all_cols=t_all_cols[:], ind=[ind[0] - 2, ind[1] + 1])
            if ind[0] + 2 <= n - 1 and ind[1] - 1 >= 0:
                Queen_DFS(t_board=t_board[:][:], t_all_rows=t_all_rows[:], t_all_cols=t_all_cols[:], ind=[ind[0] + 2, ind[1] - 1])
            if ind[0] + 1 <= n - 1 and ind[1] + 2 <= n - 1:
                Queen_DFS(t_board=t_board[:][:], t_all_rows=t_all_rows[:], t_all_cols=t_all_cols[:], ind=[ind[0] + 1, ind[1] + 2])
            pass

        for i in range(1, n):
            # try to make a possible board in line 1
            # Queen_DFS(t_board=board[:][:], t_all_rows=all_rows[:], ind=[0, i])
            print()
            Queen_DFS(t_board=[i.copy() for i in board], t_all_rows=all_rows[:], t_all_cols=all_cols[:], ind=[0, i])
        for i in answers:
            print("=" * 40)
            for j in i:
                print(j)

    def solve_N_Queens_read_answer(self, n: int) -> [[str]]:
        # row_visited = [False for i in range(n)]
        # col_visited = [False for i in range(n)]
        # # how to visit the No.x diag? i + j = x
        # diag_visited = [False for i in range((n * 2) - 1)]
        # udiag_visited = [False for i in range((n * 2) - 1)]
        answer = []

        def QueenDFS(row_n: int, t_row_visited: [bool], t_col_visited: [bool], t_diag_visited: [bool], t_udiag_visited: [bool], queen_pos: [[int, int]]):
            if row_n > n - 1:
                return
            # else: check if the queen can place
            for col_n in range(n):  # a col in line row_n, so the position is: [row_n, col_n]
                if t_row_visited[row_n] or t_col_visited[col_n] or t_diag_visited[row_n + col_n] or t_udiag_visited[n - row_n + col_n - 1]:
                    continue
                else:
                    queen_pos.append([row_n, col_n])
                    t_row_visited[row_n] = True
                    t_col_visited[col_n] = True
                    t_diag_visited[row_n + col_n] = True
                    t_udiag_visited[n - row_n + col_n - 1] = True
                    QueenDFS(row_n + 1, t_row_visited[:], t_col_visited[:], t_diag_visited[:], t_udiag_visited[:], queen_pos[:])
            # if reached the bottom
            if row_n == n - 1:
                # save answer
                print(queen_pos)
                answer.append(queen_pos)

            print("*" * 30)
            pass

        for i in range(n):
            print(i)
            row_visited = [False for i in range(n)]
            col_visited = [False for i in range(n)]
            # how to visit the No.x diag? i + j = x
            diag_visited = [False for i in range((n * 2) - 1)]
            udiag_visited = [False for i in range((n * 2) - 1)]
            # the first line, queen can be placed at any col
            row_visited[0] = True
            col_visited[i] = True
            diag_visited[0 + i] = True
            udiag_visited[n - 0 + i - 1] = True
            queen_pos = [[0, i]]
            QueenDFS(1, row_visited[:], col_visited[:], diag_visited[:], udiag_visited[:], queen_pos[:])

        print("Answers: ")
        for i in answer:
            print(i)

        # generate board:
        boards = []
        max_len = max(len(x) for x in answer)
        print(max_len)
        answer_pure = []
        for x in answer:
            if len(x) == max_len:
                answer_pure.append(x)
        print(answer_pure)
        for one in answer_pure:
            print()
            board = []
            for i in range(n):
                board.append(['.' for i in range(n)])
            for i in one:
                board[i[0]][i[1]] = 'Q'
            boards.append(board)

        return boards

        pass

    def solve_Queens(self, n: int) -> [[int]]:
        answer = []

        def generateBoard(queen_pos) -> [[str]]:
            board = []
            for i in range(n):
                line = ""
                for j in range(n):
                    if [i, j] in queen_pos:
                        line += "Q"
                    else:
                        line += "."
                board.append(line)
            return board


        def DFS(row: int):
            if row == n:
                board = generateBoard(queen_pos)
                answer.append(board)
            else:
                # check this row
                for col in range(n):
                    if row_visited[row] or col_visited[col] or diag_visited[col + row] or udiag_visited[n - row + col - 1]:
                        continue
                    else:
                        row_visited[row] = True
                        col_visited[col] = True
                        diag_visited[row + col] = True
                        udiag_visited[n - row + col - 1] = True
                        queen_pos.append([row, col])
                        DFS(row + 1)
                        queen_pos.pop(-1)
                        row_visited[row] = False
                        col_visited[col] = False
                        diag_visited[row + col] = False
                        udiag_visited[n - row + col - 1] = False
            pass  # end DFS

        row_visited = [False for i in range(n)]
        col_visited = [False for i in range(n)]
        diag_visited = [False for i in range(2 * n - 1)]
        udiag_visited = [False for i in range(2 * n - 1)]
        queen_pos = []
        DFS(0)

        return answer




n = N_Queens()
# n.solveNQueens_2()
print(n.solve_Queens(4))
