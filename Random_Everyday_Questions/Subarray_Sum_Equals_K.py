import collections


class SumEqualsK:
    # CAUTION: Simple slide-window algorithm seems won't work
    def subarraySum(self, nums: [int], k: int) -> int:
        # Make the array of prefix sum
        prefix = [0]
        count = 0  # count for the subarray whose sum equals to k
        for num in nums:
            prefix.append(prefix[-1] + num)
        # try to find k
        former, latter = 0, 1
        while former <= latter and latter <= len(prefix) - 1 and former <= len(prefix) - 1:
            gap = prefix[latter] - prefix[former]
            if gap > k:
                former += 1
                if former >= latter:
                    latter += 1
            elif gap < k:
                latter += 1
            else:
                count += 1
                latter += 1
        return count

    # Timeout
    def subarray_sum2(self, nums: [int], k: int) -> int:
        prefix = [0]
        count = 0
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
            for j in range(len(prefix) - 1):
                if prefix[-1] - prefix[j] == k:
                    count += 1
        return count

    def subarray_sum_solution_by_someone_else(self, nums: [int], k: int) -> int:
        count = 0
        n = len(nums)
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        presum = 0
        for i in range(n):
            presum += nums[i]  # compute the prefix
            count += prefix[presum - k]

            prefix[presum] += 1

        return count


s = SumEqualsK()
# print(s.subarraySum([1, 2, 3, 4, 5], 5))
# print(s.subarraySum([-1, -1, 1], 0))
# print(s.subarray_sum2([1, 2, 3, 4, 5], 5))
# print(s.subarray_sum2([1], 0))
print(s.subarray_sum_solution_by_someone_else([1, 2, 3, 4, 5], 5))
