import math


class LeetCode_Weekly:
    '''
    This is all the questions about leetcode weekly competition, which is what i am simply interested in, no else usage
    or determine.
    '''

    def convert_to_temperature(self, celsius: float) -> [float]:
        return [celsius + 273.5, celsius * 1.80 + 32.00]

    def subarray_LCM(self, nums: [int], k: int) -> int:
        # Number of subarrays with LCM eauql to K
        # How to get the LCM?   lcm(a, b) = a * b / gcd(a, b), which is included in math.lcm()...
        # first count the single element
        # TODO：wont work， figure out another solution
        count = nums.count(k)
        former, latter = 0, 1
        while latter <= len(nums) - 1:
            lcm = math.lcm(nums[latter - 1], nums[latter])
            if lcm == k:
                latter += 1
                count += 1
                continue
            else:
                if former == latter:
                    former = latter + 1
                    latter = former + 1
                    continue
                else:
                    former += 1
        pass
        return count

    # Use pure enumeration
    def sub_array_lcm(self, nums: [int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            res = 1
            for j in range(i, n):
                res = math.lcm(nums[j], res)
                if k % res: break
                if res == k:
                    count += 1
        return count


l = LeetCode_Weekly()
# print(l.subarray_LCM([3, 6, 2, 7, 1], 6))
print(l.sub_array_lcm([3, 6, 2, 7, 1], 6))
