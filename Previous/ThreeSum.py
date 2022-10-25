class ThreeSum:
    def threesum(self, nums: [int]) -> [[int]]:
        nums = sorted(nums)
        length = len(nums)
        answer = []
        for i in range(0, length - 2):
            left = i + 1
            right = length - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif temp > 0:
                    right -= 1
                elif temp < 0:
                    left += 1

        # TODO: 去重
        result = []
        for i in answer:
            if i not in result:
                result.append(i)
        print(result)
        return result


t = ThreeSum()
print(t.threesum([-1, 0, 1, 2, -1, -4]))
