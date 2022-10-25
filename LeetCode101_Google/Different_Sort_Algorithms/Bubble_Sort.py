class BubbleSort:
    def bubbles(self, nums: [int]):
        print("Before: ", nums)
        n = len(nums)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if nums[j] < nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print("After: ", nums)
        pass

b = BubbleSort()
b.bubbles([2, 4, 1, 6, 7, 9, 3, 8, 5])
