class MergeSortedArray:
    def merge_sorted_array(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2
            print(nums1)
            return
        elif n == 0:
            nums1[:] = nums1[:m]
            print(nums1)
            return
        p1, p2 = 0, 0
        sorted = []
        while p1 < m or p2 < n:
            if p1 == m:
                sorted += nums2[p2:]
                break
            elif p2 == n:
                sorted += nums1[p1:m]
                break

            if nums1[p1] <= nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1

        nums1[:] = sorted
        print(sorted)
        print(nums1)

    def merge_sorted_array_2(self, nums1: [int], m: int, nums2: [int], n) -> None:
        # 首先检查两个数列的个数，如果有空的， 那么直接返回另外一个
        if m == 0:
            nums1 = nums2
            return
        elif n == 0:
            return
        # 两个指针分别用来定位 nums1 和 nums2
        p1 = p2 = 0
        # 建立循环开始进行排序工作
        while True:
            # 如果其中一个队列已经空了，那么只需要将另外一个队列的数据给搬运过去就好了
            # if p1 == m - 1:
            if nums1[p1] == 0:
                while p2 < n:
                    nums1[p1] = nums2[p2]
                    p1 += 1
                    p2 += 1
                nums1 = nums1[0: m + n - 1]
                return
            # 如果第二个队列已经搬运完了，由于本身是在 nums1 的基础上进行改动的，因此直接返回即可
            if p2 == n - 1:
                nums1 = nums1[0: m + n]
                return
            # 此时才开始正式进行插入的操作
            # 如果 nums1 此时指向的数字大于 nums2 此时指向的数字，那么不需要进行移动，直接向后移动一位即可
            if nums1[p1] < nums2[p2]:
                p1 += 1
                continue
            # 但是对于 nums2 大于 nums1 的情况，需要考虑到此时指向的数字是否是原来数字的问题
            else:
                nums1.insert(p1 + 1, nums2[p2])
                nums1.pop()
                # 要注意这里指针的移动操作
                p1 += 2
                p2 += 1
                continue


m = MergeSortedArray()
# m.merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
m.merge_sorted_array([2, 0], 1, [1], 1)
