from typing import Optional


class MergeTwoLists:
    def mergeTwoLists(self, list1: Optional[list], list2: Optional[list]) -> Optional[list]:
        if list1 == [] and list2 == []:
            return []
        elif not list1:
            return list2
        elif not list2:
            return list1
        a1, a2 = 0, 0
        answer = []
        while True:
            l1, l2 = len(list1), len(list2)
            if l1 > 0 and l2 > 0:
                a1, a2 = list1[0], list2[0]
                if a1 >= a2:
                    answer.append(a2)
                    list2.pop(0)
                else:
                    answer.append(a1)
                    list1.pop(0)
            elif l1 > 0:
                answer += l1
                return answer
            elif l2 > 0:
                answer += l2
                return answer

    # 用C写出来了
    def singleNumber(self, nums: [int]) -> int:
        nums.sort()
        print(nums)
        i = 0
        while i <= len(nums):
            if nums[i] != nums[i + 1]:
                return nums[i]
            else:
                i += 2
            if i == len(nums) - 1:
                return nums.pop()


c = MergeTwoLists()
a = c.singleNumber([4, 1, 2, 1, 2])
print(a)