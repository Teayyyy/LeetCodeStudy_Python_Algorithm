class Premutations:
    def premute_leetcode_solution(self, nums: [int]) -> [[int]]:
        # The whole algorithm is like a tree-search, more clearly, DFS tree searching.
        # an value to save the answer, once an iteration finished, push the array into this
        answer = []

        def back_tracking(begin: int):
            # if length meets the length of nums, means one iteration is done
            if begin == len(nums) - 1:
                # PLEASE REMEMBER: the clone strategy in Python is pretty tricky, so make sure each time
                # clone is completely-clone
                answer.append(nums[:])
                return
            # how to trace back when this slice is ended?
            # set the for-statement, when for is finished, this slice is finished.
            i = begin
            while i < len(nums):
                nums[i], nums[begin] = nums[begin], nums[i]
                back_tracking(begin + 1)
                nums[i], nums[begin] = nums[begin], nums[i]
                i += 1
            return

        back_tracking(0)
        return answer


p = Premutations()
print(p.premute_leetcode_solution([1, 2, 3, 4, 5, 6]))
