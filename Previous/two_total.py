def get_total(nums: [int], target: int):
    i = 0
    for i in range(len(nums)):
        if nums[i] > target:
            continue
        sub = target - nums[i]
        j = i + 1
        while j < len(nums):
            if nums[j] == sub:
                return [i, j]
            j += 1
        i += 1


print(get_total([3, 2, 4], 6))
