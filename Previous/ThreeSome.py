class ThreeSome:
    def threeSum(self, nums: list):
        nums.sort()
        n = len(nums) - 1
        answer = []
        for i in range(n - 2):
            left, right = i + 1, n
            while left != right:
                if nums[i] + nums[left] + nums[right] == 0 and [nums[i], nums[left], nums[right]] not in answer:
                    answer.append([nums[i], nums[left], nums[right]])
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
        return answer

    def another(self, nums: list):
        nums.sort()
        n = len(nums) - 1
        answer = []
        for i in range(n - 1):
            left, right = i + 1, n
            while left != right:
                if nums[i] + nums[left] + nums[right] == 0 and [nums[i], nums[left], nums[right]] not in answer:
                    answer.append([nums[i], nums[left], nums[right]])
                    break
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1

        return answer


t = ThreeSome()
print(t.another([0, 0, 0]))
# copy
