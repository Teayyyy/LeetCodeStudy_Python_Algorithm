def maxSubArray(nums) -> int:
    i = 0
    final_max = nums[i]
    while i < len(nums):
        max = 0
        j = i + 1
        temp = nums[i]
        while j < len(nums):
            temp += nums[j]
            if temp <= nums[i]:
                i = j + 1
                j += 2
                temp = nums[i]
                continue
            if temp > max:
                max = temp
            j += 1
        if final_max < max:
            final_max = max
        i += 1
    return final_max


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

