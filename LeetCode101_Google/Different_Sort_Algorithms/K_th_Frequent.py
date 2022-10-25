class KthFrequent:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        num_dict = dict(nums)
        print(num_dict)

    def sort_words_by_frequency(self, s: str) -> str:
        result = dict()
        for c in s:
            if c not in result:
                result[c] = 1
            else:
                result[c] += 1
        # Sort the dict by its frequency, Descending sort
        temp = sorted(result, reverse=True, key=lambda m: result[m])
        # Resort the string
        answer = ""
        for x in temp:
            answer += (x * result[x])
        return answer

    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            find = target - nums[i]
            if find in nums:
                ind = nums.index(find)
                if ind != i:
                    return [i, ind]

    def twoSum_2(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            find = target - nums[i]
            if find == nums[i] and nums.count(find) > 1:
                return [nums.index(find), nums[nums.index(find) + 1:].index(find) + nums.index(find) + 1]
            elif find == nums[i] and nums.count(find) <= 1:
                continue
            else:
                if find in nums:
                    return [i, nums.index(find)]


k = KthFrequent()
# print(k.sort_words_by_frequency("Trreee"))
# print(k.sort_words_by_frequency("JJJSKLJDKSIjsksjlljsk"))
# print(k.twoSum([2, 7, 11, 15], 9))
print(k.twoSum_2([3, 2, 3], 6))
