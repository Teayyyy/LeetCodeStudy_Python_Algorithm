class WiggleSort:
    def wiggle(self, nums: [int]) -> None:
        bucket = [0 for i in range(5001)]
        for i in nums:
            bucket[i] += 1
        i = 0
        j = 5000
        while i < len(nums):
            while bucket[j] == 0:
                j -= 1

            nums[i] = j
            bucket[j] -= 1
            i += 2

        i = 1
        while i < len(nums):
            while bucket[j] == 0:
                j -= 1

            nums[i] = j
            bucket[j] -= 1
            i += 2
        print(nums)


w = WiggleSort()
w.wiggle([1, 5, 1, 1, 6, 4])
