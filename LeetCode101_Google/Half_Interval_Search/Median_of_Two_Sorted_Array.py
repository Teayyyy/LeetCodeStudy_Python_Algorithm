class MedianOfTwoSortedArray:
    def get_median(self, nums1: [int], nums2: [int]) -> float:
        '''
        这道题考察的是二分查找，寻找两个有序数组的中位数，数组均按照升序排列
        思路：
            1、首先判断两个数组个数之和，如果为单数，那么中位数就是中间那一个，如果是双数，那么就是中间的两个数的二分之一
            2、分别找到当前两个数组段落的中间数，判断两个数的大小（其中两个数组指向的数字分别是：l1、m1、r1 / l2、m2、r2
                如果 nums1[m1] < nums2[m2]，那么代表数组中的区间：[l1, m1] 均小于 [m2, r2]，因此可以将这两区间中的所有数字分别放到两
                个不同的数组 left right中，并且计数
                PS. 当两数组个数之和为单数时候，剩余一个数即为中位数；当两数组个数之和为偶数的时候，剩余两个数的二分之一即为中位数
        :param nums1:第一个有序数组
        :param nums2: 第二个有序数组
        :return: 返回二者的中位数
        '''

        n1, n2 = len(nums1), len(nums2)
        # 判断特殊情况
        if (n1 + n2) % 2 == 1:  # 两数组个数之和为奇数
            # 如果一个数组为空
            if n1 == 0:
                return nums2[(n2 - 1) // 2]
            elif n2 == 0:
                return nums1[(n1 - 1) // 2]
            # 如果两个数组能头尾相接
            if nums1[n1 - 1] <= nums2[0]:
                return (nums1 + nums2)[(n1 + n2 - 2) // 2 + 1]
            elif nums2[n2 - 1] <= nums1[0]:
                return (nums2 + nums1)[(n1 + n2 - 2) // 2 + 1]
        elif (n1 + n2) % 2 == 0:  # 两数组之和为偶数
            # 如果一个数组为空
            if n1 == 0:
                # return nums2[(n2 - 1) // 2]
                return (nums2[(n2 - 1) // 2] + nums2[(n2 - 1) // 2 + 1]) / 2
            elif n2 == 0:
                return (nums1[(n1 - 1) // 2] + nums1[(n1 - 1) // 2 + 1]) / 2
            # 如果两个数组能头尾相接
            if nums1[n1 - 1] <= nums2[0]:
                return ((nums1 + nums2)[(n1 + n2 - 2) // 2] + (nums1 + nums2)[(n1 + n2 - 2) // 2 + 1]) / 2
            elif nums2[n2 - 1] <= nums1[0]:
                return ((nums2 + nums1)[(n1 + n2 - 2) // 2] + (nums2 + nums1)[(n1 + n2 - 2) // 2 + 1]) / 2

        # 正式开始算法
        l1, r1 = 0, n1 - 1  # 第一个数组
        l2, r2 = 0, n2 - 1  # 第二个数组
        remain = n1 + n2  # 还剩下的数字个数，总数为单数的时候需要剩下一个，总数为双数的时候需要剩下两个
        left, right = 0, 0  # 用来保存两侧已有数字的个数
        while l1 <= r1 and l2 <= r2:
            m1 = (l1 + r1) // 2
            m2 = (l2 + r2) // 2
            # 判断 m1 和 m2 所指数据的大小
            if nums1[m1] == nums2[m2]:  # 相等的时候，分别往 left 和 right 放数
                left += (m1 - l1 + m2 - l2)
                right += (r1 - m1 + r2 - m2)
                # 相等后，m1，m2两侧的所有数据都会放到 left 和 right 中，仅留下 m1，m2 未确定
                if left == right:  # 此时肯定是偶数个才会出现两侧相等剩下两个的情况
                    return (nums1[m1] + nums2[m2]) / 2
                pass
            elif nums1[m1] > nums2[m2]:
                # if l1 == r1:
                #     left += (m2 - l2)
                #     pass
                # elif l2 == r2:
                #     pass
                # else:
                #     right += (r1 - m1)
                #     left += (m2 - l2)
                # pass
                right += (r1 - m1)
                left += (m2 - l2)
                r1 = m1
                l2 = m2
            elif nums1[m1] < nums2[m2]:  # 这会儿 [l1, m1]放入left， [m2, r2]放入 right
                left += (m1 - l1)
                right += (r2 - m2)
                l1 = m1
                r2 = m2
                pass
            # TODO:判断有一个数组仅剩一个数的情况
            if l1 == r1 and n1 + n2 - left - right == 3:
                newarr = [nums1[l1], nums2[l2], nums2[r2]]
                newarr.sort()
                if left > right:
                    return newarr[0]
                elif right > left:
                    return newarr[2]
                elif left == right:
                    return newarr[1]
                pass
            elif l2 == r2 and n1 + n2 - left - right == 3:
                newarr = [nums2[l2], nums1[l1], nums1[r1]]
                newarr.sort()
                if left > right:
                    return newarr[0]
                elif right > left:
                    return newarr[2]
                elif left == right:
                    return newarr[1]
                pass
            # 判断 n 的奇偶
            if (n1 + n2) % 2 == 0 and (n1 + n2) - left - right == 2:  # 偶数
                return (nums1[m1] + nums2[m2]) / 2
                pass
            elif (n1 + n2) % 2 == 1 and (n1 + n2) - left - right == 2:  # 奇数
                if left < right:
                    return nums2[m2]
                elif right < left:
                    return nums1[m1]
                pass

        print("Error, Jumped out the loop")
        pass


m = MedianOfTwoSortedArray()
print(m.get_median([1, 3], [2, 7]))
# print(m.get_median([1,3],[2]))
'''
见网址：https://leetcode.cn/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
'''

# 特殊情况测试
# print(m.get_median([1, 2, 3, 4], [5, 6, 7, 8, 9]))
# print(m.get_median([1, 2, 3, 4], [5, 6, 7, 8]))
# print(m.get_median([5, 6, 7, 8, 9], [1, 2, 3, 4]))
# print(m.get_median([5, 6, 7, 8], [1, 2, 3, 4]))
# print(m.get_median([1, 2, 3], []))
# print(m.get_median([1, 2, 3, 4], []))
# print(m.get_median([], [1, 2, 3]))
# print(m.get_median([], [1, 2, 3, 4]))
# print(m.get_median([1, 2, 3, 4, 5, 6], []))
# print(m.get_median([], [1, 2, 3, 4, 5, 6]))
