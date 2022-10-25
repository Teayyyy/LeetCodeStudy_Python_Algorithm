class FindKthLargest:
    def find_in_bubble_sort(self, nums, k) -> int:
        print("original", end=": ")
        print(nums)
        saved = []
        temp_list = nums
        for i in range(k):
            temp_index = 0
            for j in range(0, len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                # if nums[j] < nums[temp_index]:
                #     nums[j], nums[temp_index] = nums[temp_index], nums[j]
                #     temp_index = j
            print("**********" + str(nums))
        print(nums)
        return nums[len(nums) - k]

    def find_in_quick_sort(self, nums, k) -> int:
        # TODO: 看 iPad 上的内容
        # 题目地址: https://leetcode.cn/problems/kth-largest-element-in-an-array/
        '''
        因为要找最大的第 K 个元素，因此使用二分查找和快速排序叠加的方式进行排序
        当一次快速查找（排序）完成时，当前元素（Pivot）左侧均比其小，右侧均比其大，因此查找当前 Pivot 的索引
        如果正好是第 K 大（左侧第 K 个或右侧第 K 个）那么则查找成功，如果不是，则判断大小
            如果索引偏小，则将 l 设置 mid + 1， 索引偏大则 r 设置为 mid - 1
        '''
        # 首先进行二分查找
        print(sorted(nums))
        l = 0
        r = len(nums) - 1
        # 查找的位置，为第 K 大的元素（默认排序是从小到大的顺序）
        target = r - k
        while l < r:
            print("while l < r")
            # mid = self.quick_selection(nums, l, r)
            mid = self.my_quick_selection(nums, l, r)
            if mid == target:
                return nums[target]
            elif mid < target:
                l = mid + 1
            elif mid > target:
                r = mid - 1
        # return nums[l]
        # 因为这里有重复的数字

    def quick_selection(self, nums: [int], l: int, r: int) -> int:
        # 进行一轮快速选择（排序）
        i = l + 1
        j = r
        while i < j:
            print("while quick sort, i: {0}, j: {1}".format(i, j))
            while nums[i] < nums[l] and i < r:
                i += 1
            while nums[j] > nums[l] and l < j:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[l], nums[j] = nums[j], nums[l]
        return j
        pass

    def my_quick_selection(self, nums: [int], l: int, r: int) -> int:
        # do a quick sort
        i = l
        j = r
        temp = nums[l]
        while True:
            if l >= r:
                break
            while nums[r] > temp and r > i:
                r -= 1
            if r > i:
                nums[l] = nums[r]
                l += 1
            while nums[l] < temp and l < j:
                l += 1
            if l < j:
                nums[r] = nums[l]
        return l

    def my_test(self, nums: [int], k: int) -> int:
        print(sorted(nums))
        # 设定冒泡算法，每次放出当前最大的元素，但是需要考虑到重复的元素
        single = set()
        count = 0
        while len(single) < k:
            # 开始冒泡算法
            temp = 0
            for i in range(len(nums) - count - 1):
                if nums[i] > nums[i + 1]:
                    # swap i and i + 1
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                temp = i + 1
            # put the current biggest one into the set
            # print("Temp num[i + 1]: ", nums[i + 1])
            # print("i + 1: ", i + 1)
            if nums[temp] not in single:
                single.add(nums[temp])
            count += 1
        print(single)
        return min(single)

    # 运行成功，但是 leetcode 超长数组不通过，超出时间限制
    def my_largest_kth_number(self, nums: [int], k: int) -> int:
        print(sorted(nums))
        # set an array in this rule: only the current largest K numbers will be saved
        saved = []  # only saved largest k numbers
        # def insert_sort(item):
        #     for i in range(len(saved)):
        #         if saved[i] > item:
        #             if i == 0:
        #                 saved = item + saved
        #             else:
        #                 saved.insert(i - 1, item)
        #         if saved[i] < item and i == len(saved) - 1:
        #             saved += item
        # Insert Sort
        for item in nums:
            if len(saved) == 0:
                saved.append(item)
            else:
                for i in range(len(saved)):
                    if saved[i] > item:
                        if i == 0:
                            saved.insert(0, item)
                            break
                        else:
                            saved.insert(i, item)
                            break
                    if saved[i] <= item and i == len(saved) - 1:
                        saved.append(item)
            if len(saved) > k:  # when the length of the saved is smaller than K, just append in insert sort
                saved = saved[1:]
        print(saved)
        return min(saved)

    # 自己手写的 分治 + 快速选择
    def my_largest(self, nums: [int], k: int) -> int:
        print(sorted(nums))
        # Using binary search should be the quickest method, like below:
        # On each quick selection, the pivot element should on the right position of its own, and method will return its
        # index, if the return position(sorted increasingly) is not right, select the next element on left(bigger) and
        # right(smaller), and make sure THE NUMS ITSELF IS RETURNED WITH THE METHOD!
        left, right = 0, len(nums) - 1
        target = len(nums) - k
        # TODO: There must set to: left <= right  Figure it out why
        while left <= right:
            mid, nums = self.my_quick_selection_rewrite_2(nums, left, right)
            if mid == target:
                return nums[mid]
            elif mid < target:
                left = mid + 1
            elif mid > target:
                right = mid - 1
        pass

    # 你的 quickSelection 函数存在问题！！！！ Warning
    def my_quick_selection_rewrite(self, nums: [int], l: int, r: int):
        # 快速选择，在选择完成后当前的 pivot 元素的左右两侧分别为小于和大于的元素
        pivot = nums[l]
        # l += 1
        while True:
            print("l: {0}, r: {1}".format(l, r))
            if l >= r:
                break
            # Find one element that is smaller than pivot on r side
            while l < r and nums[r] > pivot:
                r -= 1
            # Swap the l and r element
            nums[l] = nums[r]
            # Now l element is on its right position, so l += 1
            l += 1
            # And then find one element that is bigger than pivot on l side
            while l < r and nums[l] < pivot:
                l += 1
            # Swap
            nums[r] = nums[l]
            r -= 1
        # When this loop finished, the position of the pivot should lay on l/r(they are on same position)
        nums[l] = pivot
        # print(nums)
        # print(l,r, sep=" | ")
        return l, nums
        pass

    def my_quick_selection_rewrite_2(self, nums: [int], l: int, r: int):
        former = l
        latter = r
        pivot = nums[l]
        while True:
            while latter > l and nums[latter] >= pivot:
                latter -= 1
            # change
            if former >= latter:
                nums[former] = pivot
                return former, nums
                # break
            nums[latter], nums[former] = nums[former], nums[latter]
            while former < r and nums[former] <= pivot:
                former += 1
            # change
            if former >= latter:
                nums[latter] = pivot
                return latter, nums
                # break
            nums[former], nums[latter] = nums[latter], nums[former]
        # print("former: {0}, latter: {1}".format(former, latter))
        # print(nums)


    # TODO: 自己写出快速选择算法（用上面的逻辑），在写出下面的快速选择算法
    def quickSelection(self, nums: [int], l: int, r: int):
        i = l + 1
        j = r
        while True:
            while i < r and nums[i] <= nums[l]:
                i += 1
            while l < j and nums[j] >= nums[l]:
                j -= 1

            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[l], nums[j] = nums[j], nums[l]
        return j, nums


find = FindKthLargest()
# print(find.my_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
# print(find.my_largest([3, 2, 1, 5, 6, 4], 2))
print(find.my_largest([2, 1], 2))
# print(find.my_quick_selection_rewrite_2([3, 2, 3, 1, 2, 4, 5, 5, 6], 0, 7))

