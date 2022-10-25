class SearchRotatedArray:
    def searchArray_own(self, nums: [int], target: int) -> bool:
        # 直接用 python 内置函数来找，但是没有用到自己的想法
        return nums.count(target) > 0


