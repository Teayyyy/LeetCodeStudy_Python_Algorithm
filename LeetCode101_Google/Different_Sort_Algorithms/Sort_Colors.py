class SortColors:
    def sort_colors(self, nums: [int]) -> None:
        nums1 = nums.copy()
        print("Before: ", nums1)
        # if current element is 0, move it to the head of the array, if it is 2, move it to the end
        end = len(nums1)
        temp = 0
        while temp < end:
            if nums1[temp] == 1:
                temp += 1
                continue
            elif nums1[temp] == 0:
                # Move to the head
                nums1.pop(temp)  # delete this element
                # add to the head
                nums1 = [0] + nums1
                # move pointer
                temp += 1
                pass
            elif nums1[temp] == 2:
                # Move to the end
                nums1.pop(temp)
                nums1 = nums1 + [2]
                # No need to move pointer, but need to move end
                end -= 1
                pass
        nums = nums1
        print("After: ", nums1)

    def sort_colors_2(self, nums: [int]):
        result = [0, 0, 0]
        for i in nums:
            if i == 0:
                result[0] += 1
            elif i == 1:
                result[1] += 1
            elif i == 2:
                result[2] += 1
        for i in range(len(nums)):
            if result[0] > 0:
                nums[i] = 0
                result[0] -= 1
            elif result[0] == 0 and result[1] > 0:
                nums[i] = 1
                result[1] -= 1
            elif result[0] == 0 and result[1] == 0 and result[2] > 0:
                nums[i] = 2
                result[2] -= 1
        print(nums)


s = SortColors()
# s.sort_colors([2, 2, 1, 1, 2, 1, 2, 1, 0, 0, 1, 0, 1, 0, 1, 2, 2, 1, 0, 2])
s.sort_colors_2([2, 0, 2, 1, 1, 0])
