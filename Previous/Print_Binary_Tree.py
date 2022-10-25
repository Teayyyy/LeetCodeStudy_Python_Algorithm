from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PrintBinaryTree:
    def __init__(self):
        self.res = [[]]
        self.m = 0
        self.n = 0
    def print_Tree(self, root: Optional[TreeNode]) -> [[str]]:
        # get the depth of the BTree
        height = int(math.log2(len(root))) + 1
        # got the height and the length of the matrix
        m = height
        n = (2 ** height) - 1
        res = [["" for i in range(n)] for j in range(m)]
        waiting_queue = []
        # using the Hierarchical Traversal
        res[0][(n - 1) // 2] = root[0]
        # waiting_queue.append(root[0])
        # while waiting_queue:
        #     temp_node = waiting_queue.pop(0)
        #
        for i in range(len(root)):
            if i == 0:
                res[0][(n - 1) // 2] = root[i]
                # gap_side = (n - 1) // 2  # How many gaps on each side, which is equal to the middle gap in next line
            tmp_h = int(math.log2(i + 1)) + 1

        return res

    def print_tree(self, root: Optional[TreeNode]) -> [[str]]:
        height = int(math.log2(len(root))) + 1
        self.m = height
        self.n = (2 ** height) - 1
        self.res = [["" for i in range(self.n)] for j in range(self.m)]
        # recursive
        self.set_tree(root, 0, (self.n - 1) // 2)
        for line in self.res:
            print(line)
        pass

    def set_tree(self, root: Optional[TreeNode], i: int, j: int):
        # set the position of this node
        self.res[i][j] += root.val
        if root.left:
            self.set_tree(root.left, i + 1, j - 2 ** (self.m - i - 1))
            pass
        if root.right:
            self.set_tree(root.right, i + 1, j + 2 ** (self.m - i - 1))
            pass

        if root.left and root.right:
            return




p = PrintBinaryTree()
print(p.print_tree([1, 2, 3, None, 4]))
