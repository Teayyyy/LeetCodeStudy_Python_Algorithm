class ShortestSubArray:
    # Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of
    # nums with a sum of at least k. If there is no such subarray, return -1
    def shortest_at_least_K(self, nums: [int], k: int) -> int:
        # This is a Hard-level code!
        # Here are what I'm thinking: making an slidable-window, once the sum of window passes k, left move,
        # if not, right move
        # init length, defaulted by -1
        max_len = len(nums) + 1
        former, latter = 0, 0
        while latter <= len(nums) - 1:
            temp_sum = sum(nums[former: latter + 1])
            if temp_sum >= k:
                max_len = min(max_len, latter - former + 1)
                former += 1
                latter -= 1
            latter += 1
        return max_len if max_len < len(nums) + 1 else -1
        # return max_len

    def shotest_K(self, nums: [int], k: int) -> int:
        max_len = len(nums) + 1
        former, latter = 0, 0
        while latter <= len(nums) - 1:
            temp_sum = sum(nums[former: latter + 1])
            # This method can't deal with negative numbers
            while temp_sum >= k and latter <= len(nums) - 1 and former <= len(nums) - 1:
                temp_sum = sum(nums[former: latter + 1])
                max_len = min(max_len, latter - former + 1)
                former += 1
            latter += 1
        return max_len if max_len < len(nums) + 1 else -1

    # this method is trying to elevate every number to the positive number DO NOT WORK!
    def shortest_k_with_all_positive(self, nums: [int], k: int) -> int:
        # make each number bigger than 0
        min_num = abs(min(nums))
        new_num = [i + min_num for i in nums]
        new_k = k + min_num
        print(new_num)
        print(new_k)
        # find smallest subarray
        min_len = len(nums) + 1
        former, latter = 0, 0
        while latter <= len(nums) - 1:
            temp_sum = sum(new_num[former: latter + 1])
            while temp_sum >= new_k and latter <= len(new_num) - 1 and former <= len(nums) - 1:
                temp_sum = sum(new_num[former: latter + 1])
                min_len = min(min_len, latter - former + 1)
                former += 1
            latter += 1
        return min_len if min_len <= len(nums) + 1 else -1

    # this needs double-edge-queue and presum_array, solution on the leetcode are as below:
    def shortest_k_with_official_solution(self, nums: [int], k: int) -> int:
        # TODO: see leetcode solution
        # 1.https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/solution/python3-on-qian-zhui-he-tu-jie-by-accsrd-uhf4/
        # 2.https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/solution/python-dan-diao-dui-lie-bi-guan-fang-ti-cywko/
        pass



shotest = ShortestSubArray()
# print(shotest.shortest_at_least_K(nums=[2, -1, 2], k=3))
# print(shotest.shortest_at_least_K([1], 1))
# print(shotest.shortest_at_least_K([48, 99, 37, 4, -31], 140))
# print(shotest.shortest_at_least_K([84, -37, 32, 40, 95], 167))
# print(shotest.shotest_K([1], 1))
# print(shotest.shotest_K(nums=[2, -1, 2], k=3))
print(shotest.shortest_k_with_all_positive([84, -37, 32, 40, 95], 167))
