class Solution:
    def maxArea(self, height: [int]) -> int:
        # 采用双指针算法
        max_val = 0
        left, right = 0, len(height) - 1
        while left != right:
            volume = min(height[left], height[right]) * (right - left)
            max_val = max(volume, max_val)
            print("left: {0}, right:{1} = {2}".format(height[left], height[right], volume))
            if height[left] <= height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
        return max_val


s = Solution()
a = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
# a = s.maxArea([2, 3, 4, 5, 18, 17, 6])
print(a)
