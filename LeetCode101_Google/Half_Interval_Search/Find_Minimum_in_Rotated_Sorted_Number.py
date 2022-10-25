class FindMinimumNumber:
    def find_minimum(self, nums: [int]) -> int:
        # 如果是递增序列，那么对于 former, latter, mid 来说，根据题中的数组特性，那么一定是:
        # num[former] < num[latter] 或 num[mid] < num[latter]，如果有一边的大小变了那么说明在区间[a, b]内会有更小的数字，进去继续查找
        if len(nums) is 1:
            return nums[0]
        elif len(nums) is 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        former, latter = 0, len(nums) - 1
        while former < latter:
            mid = (former + latter) // 2
            if nums[former] <= nums[mid] <= nums[latter]:
                return nums[former]
            elif former is mid or latter is mid:
                if former < latter:
                    return nums[former]
                else:
                    return nums[latter]
            elif nums[former] < nums[mid] and nums[mid] > nums[latter]:
                former = mid + 1
            elif nums[former] > nums[mid] and nums[mid] < nums[latter]:
                latter = mid - 1

    def find_minimum_2(self, nums: [int]) -> int:
        # 如果是递增序列，那么对于 former, latter, mid 来说，根据题中的数组特性，那么一定是:
        # num[former] < num[latter] 或 num[mid] < num[latter]，如果有一边的大小变了那么说明在区间[a, b]内会有更小的数字，进去继续查找
        if len(nums) is 1:
            return nums[0]
        elif len(nums) is 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        former, latter = 0, len(nums) - 1
        while former < latter:
            mid = (former + latter) // 2
            if nums[former] <= nums[mid] < nums[latter]:  # 前两个 if 需要考虑到不同的情况，因为两个返回的位置不同
                return nums[former]
            elif nums[former] >= nums[mid] > nums[latter]:
                return nums[latter]
            elif nums[former] < nums[mid] and nums[mid] > nums[latter]:
                former = mid  # 仍然需要考虑到 mid，不能将其排除在外（也是递增 / 递减的一环）
            elif nums[former] > nums[mid] and nums[mid] < nums[latter]:
                latter = mid


f = FindMinimumNumber()
# print(f.find_minimum([3, 4, 5, 1, 2]))
# print(f.find_minimum([4, 5, 6, 7, 0, 1, 2]))
# print(f.find_minimum([11, 13, 15, 17]))
# print(f.find_minimum([2, 1]))
# print(f.find_minimum([3, 1, 2]))

print(f.find_minimum_2([3, 4, 5, 1, 2]))
print(f.find_minimum_2([3, 1, 2]))
print(f.find_minimum_2([2, 1]))
print(f.find_minimum_2([4, 5, 6, 7, 8, 0, 1, 2]))

