class InsertionSort:
    def my_insert_sort(self, nums: [int]):
        print("Unsorted: ", nums)
        # 从头到尾开始逐个放到合适的位置去
        p = 1
        while p <= len(nums):
            # print("while1")
            temp = p - 1
            while temp > 0:
                # print("while 2")
                if nums[temp] < nums[temp - 1]:
                    nums[temp], nums[temp - 1] = nums[temp - 1], nums[temp]
                temp -= 1
            p += 1
        print("Sorted: ", nums)

    def lengthOfLastWord(self, s: str) -> int:
        # this will return the length of the last word in certain string
        print(s.split())
        return 1

    def searchInsert(self, nums: [int], target: int) -> int:
        n = len(nums)
        former, latter = 0, n - 1
        while former <= latter:
            mid = (former + latter) // 2
            if nums[mid] == target:
                return former
            elif nums[mid] < target:
                former = mid + 1
            elif nums[mid] > target:
                latter = mid - 1
        return former


ii = InsertionSort()
# ii.my_insert_sort([2, 4, 1, 6, 7, 9, 3, 8, 5])
# print(ii.lengthOfLastWord(" fly me to the moon "))
# print(ii.lengthOfLastWord("a"))
print(ii.searchInsert([1, 3, 5, 6], 4))
