from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Construct_Binary_Tree:
    def constructMaximumBinaryTree(self, nums: [int]) -> Optional[TreeNode]:
        '''
        构建最大子树的方法：
            1、创建一个根结点，其值为 nums 中的最大值
            2、递归地在最大值左边的 子数组 上构建左子树
            3、递归地在最大值右边的 子数组 上构建右子树
            返回 nums 构建的最大二叉树
        '''
        if len(nums) == 0:
            return None
        # get the maximum number in this array to form the root node
        max_val = TreeNode(max(nums), None, None)
        # make the left subarray and right subarray to its child node
        max_ind = nums.index(max_val.val)
        # do this method recursively
        if max_ind - 1 >= 0:
            max_val.left = self.constructMaximumBinaryTree(nums[0: max_ind])
        if max_ind + 1 < len(nums):
            max_val.right = self.constructMaximumBinaryTree(nums[max_ind + 1:])

        return max_val


c = Construct_Binary_Tree()
c.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])

