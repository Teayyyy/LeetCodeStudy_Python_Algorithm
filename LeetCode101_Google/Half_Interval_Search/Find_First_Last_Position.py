class FindFirstAndLastPosition:
    def search_range(self, nums: [int], target: int) -> [int]:
        # 这道题类似于自己实现 C++ 里的 upperBound 和 lowerBound 函数
        left, right = 0, len(nums) - 1
        if right == -1:
            return [-1, -1]
        elif right == 0:
            if nums[0] is not target:
                return [-1, -1]
            elif nums[0] is target:
                return [0, 0]
        mid = 0
        while left <= right:
            # 获取中间点
            mid = (left + right) // 2
            # 判断是否找到了当前所需数字的区间
            if nums[mid] == target:
                break  # 此时 mid 的值就是数字 target 的区间
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if left >= right and nums[mid] is not target:
            return [-1, -1]

        # 查找左右边界
        l_over, r_over = False, False
        left, right = mid, mid
        while not l_over or not r_over:
            if left - 1 >= 0 and nums[left - 1] is target:
                left -= 1
            else:
                l_over = True

            if right + 1 < len(nums) and nums[right + 1] is target:
                right += 1
            else:
                r_over = True

        return [left, right]


f = FindFirstAndLastPosition()
# print(f.search_range(nums=[5, 7, 7, 8, 8, 10], target=8))
print(f.search_range(nums=[2, 2], target=2))
