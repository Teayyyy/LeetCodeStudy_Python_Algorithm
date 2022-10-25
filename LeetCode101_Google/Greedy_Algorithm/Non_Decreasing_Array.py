class NonDecreasingArray:
    def non_decreasing_array(self, nums: [int]) -> bool:
        if len(nums) == 1:
            return True
        modified = False  # 判断是否已经更改过，只能更改一次
        for i in range(len(nums)):
            # 在第一个位置出现了递减
            if i == 0:
                if nums[i] > nums[i + 1]:
                    nums[i] = nums[i + 1]
                    modified = True
            # 最后一个位置出现了递减
            elif i == len(nums) - 1:
                if nums[i - 1] > nums[i]:
                    if modified:  # 只能更改一次
                        return False
                    else:
                        nums[i] = nums[i - 1]
                        modified = True
            # 这时候都是中间出现递减的情况，要改变的话，需要决定修改 i 还是 i + 1，需要考虑三个地方，瞻前顾后
            else:
                if nums[i] > nums[i + 1]:
                    if modified:
                        return False
                    # 首先考虑缩小前面，不要放大后面，否则后面更难以实现非递减
                    if nums[i - 1] <= nums[i + 1]:
                        nums[i] = nums[i + 1]
                    else:
                        nums[i + 1] = nums[i]
                    modified = True
        return True


n = NonDecreasingArray()
print(n.non_decreasing_array([1, 4, 1, 2]))
