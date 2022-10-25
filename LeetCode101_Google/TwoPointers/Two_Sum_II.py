class TwoSumII:
    def two_sum_II(self, numbers: [int], target: int) -> [int]:
        # 使用双指针的思想来解决
        former, latter = 0, 1
        n = len(numbers)
        if n == 2:
            return [0, 1]
        while former < n:
            if numbers[former] + numbers[latter] == target:
                return [former, latter]
            if latter == n - 1:
                former += 1
                latter = former + 1
                continue
            latter += 1

        # 上面这个方法会超时

    def official_solution(self, numbers: [int], target: int) -> [int]:
        # 因为整个数组是非递减的数组，因此可以用双指针的思想来做!!!!!
        # 思想方法：将两个指针分别从头尾开始遍历，如果等于 target， 那么就是我们要找的元素，如果当前的结果小于 target， 则表明需要更大的元素，
        # 因此将 前面的元素向后移动一个； 吐过当前结果大于 target，则证明当前需要更小的元素，则将末尾的元素向前移动一个
        if len(numbers) == 2:
            return [1, 2]
        former, latter = 0, len(numbers) - 1
        while former < latter:
            temp_sum = numbers[former] + numbers[latter]
            if temp_sum == target:
                return [former + 1, latter + 1]
            elif temp_sum < target:
                former += 1
            elif temp_sum > target:
                latter -= 1


t = TwoSumII()
print(t.two_sum_II_2([1, 2, 3, 4, 4, 9, 56, 90], 8))
