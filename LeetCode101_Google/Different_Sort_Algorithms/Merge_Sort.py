class MergeSort:
    def __init__(self, nums: [int]):
        self.nums = nums

    def my_merge_sort(self):
        print("Before: ", self.nums)
        begin = 0
        end = len(self.nums) - 1
        self.merge_detail_2(begin, end)
        print("After: ", self.nums)
        pass

    def merge_detail(self, begin: int, end: int):
        # 判断递归返回
        if begin >= len(self.nums) or end > len(self.nums):
            return
        if begin == end:
            return
        # 对数组进行进一步的分割
        middle = (begin + end) // 2
        # 将数组拆分为两段，分别递归
        self.merge_detail(begin, middle)
        self.merge_detail(middle + 1, end)
        # 当执行到这里的时候，[begin, middle] [middle + 1, end]为已经排序好的数组
        num1 = self.nums[begin: middle]
        num2 = self.nums[middle: end]
        # 执行这个子数组的排序
        result = []
        p1, p2 = 0, 0
        while True:
            # 如果出现了一个数组已经排序完成的情况
            if p1 >= len(num1):
                result += num2[p2:]
                break
            elif p2 >= len(num2):
                result += num1[p1:]
                break
            if num1[p1] <= num2[p2]:
                result.append(num1[p1])
                p1 += 1
            else:
                result.append(num2[p2])
                p2 += 1
        # 排序完成后替换原来的数组
        # print(result)
        # result.sort()
        # print(result)
        self.nums[begin: end] = result

        pass

    def merge_detail_2(self, begin: int, end: int):
        if begin >= len(self.nums) or end > len(self.nums):
            return
        if begin == end:
            return
        # 将数组一分为二
        middle = (begin + end) // 2
        self.merge_detail_2(begin, middle)
        self.merge_detail_2(middle + 1, end)
        num1 = self.nums[begin: middle + 1]
        num2 = self.nums[middle + 1: end + 1]
        print("temp array: ")
        print(num1)
        print(num2)
        p1, p2 = 0, 0
        result = []
        while True:
            if p1 >= len(num1):
                result += num2[p2:]
                break
            elif p2 >= len(num2):
                result += num1[p1:]
                break
            if num1[p1] <= num2[p2]:
                result.append(num1[p1])
                p1 += 1
            elif num2[p2] < num1[p1]:
                result.append(num2[p2])
                p2 += 1
        # 更改原来的数组
        self.nums[begin: end + 1] = result


# m = MergeSort([8, 4, 5, 7, 1, 3, 6, 2])
m = MergeSort([2, 4, 1, 6, 2, 7, 9, 3, 8])
m.my_merge_sort()
