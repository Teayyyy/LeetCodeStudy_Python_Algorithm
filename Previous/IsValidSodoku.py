class IsValidSoduKu:
    def is_valid(self, board: [[str]]) -> bool:
        # 判断行、列
        count = 0
        for row in board:
            check_list = []
            for item in row:
                in_row = count // 9
                in_col = count % 9
                print(in_row, in_col, sep="  ")
                count += 1

                # 检查九宫格，仅在九宫格第一格的时候检查
                if in_row % 3 == 0 and in_col % 3 == 0:
                    print("进入九宫格检查")
                    check_nine_square = []
                    for i in range(3):
                        for j in range(3):
                            if board[in_row + i][in_col + j] == ".":
                                continue
                            if board[in_row + i][in_col + j] not in check_nine_square:
                                check_nine_square.append(board[in_row + i][in_col + j])
                            else:
                                return False

                # 纵向检查
                check_col = []
                for i in range(9):
                    print("纵向" + str(i), end=" ")
                    if board[i][in_row] == ".":
                        continue
                    if board[i][in_row] not in check_col:
                        check_col.append(board[i][in_row])
                    else:
                        return False
                print()

                if item == ".":
                    continue
                # 横向检查
                if item not in check_list:
                    check_list.append(item)
                else:
                    print("横向")
                    return False
                # 获取相对的坐标
                # in_row, in_col = board.index(row), row.index(item)

        return True

    def is_valid_2(self, board: [[str]]) -> bool:
        count = 0
        # 记录竖的矩阵
        trasive = []
        for row in range(9):
            temp = []
            for col in range(9):
                temp.append(board[col][row])
            trasive.append(temp)
        # print("previous:", end=" \n")
        # for row in board:
        #     print(row)
        # print("now:", end=" \n")
        # for row in trasive:
        #     print(row)
        for row in range(9):
            check = []
            for col in range(9):
                now = board[col][row]
                if now == ".":
                    continue
                if now not in check:
                    check.append(now)
                else:
                    return False

        count = 0
        for row in board:
            check = []
            for col in row:
                in_row = count // 9
                in_col = count % 9
                count += 1

                if in_row % 3 == 0 and in_col % 3 == 0:
                    print("进入九宫格检查")
                    check_nine_square = []
                    for i in range(3):
                        for j in range(3):
                            if board[in_row + i][in_col + j] == ".":
                                continue
                            if board[in_row + i][in_col + j] not in check_nine_square:
                                check_nine_square.append(board[in_row + i][in_col + j])
                            else:
                                return False

                if col == ".":
                    continue
                if col not in check:
                    check.append(col)
                else:
                    return False
        return True


isss = IsValidSoduKu()
matrix_1 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

matrix_2 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

matrix_3 = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]]

matrix_4 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

matrix_5 = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["8", ".", ".", ".", ".", "7", ".", ".", "."],
            [".", ".", ".", "8", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "9", ".", "2", ".", "5"],
            ["8", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "3", ".", ".", "6", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "8", "."],
            [".", ".", "9", ".", ".", ".", ".", ".", "."]]

matrix_6 = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]
]

# answer = isss.is_valid(matrix_5)
answer = isss.is_valid_2(matrix_6)

print(answer)
