class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class InOrderSuccessor:

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        return None


ins = InOrderSuccessor()
ins.inorderSuccessor(TreeNode(5, None, None), )

a = [1, 2, 4, 5, 6, 6, 6]
print(a[a.index(2)])
