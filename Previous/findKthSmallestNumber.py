class FindKthSmallestNumber:
    def finding(self, m: int, n: int, k: int) -> int:
        if k == 1:
            return 1
        if k == m * n:
            return m * n

        left, right = 1, m * n
        while left < right:
            mid = (left + right) // 2
            if self.count_nums(m, n, mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left

    def count_nums(self, m, n, mid) -> int:
        result = sum(min(mid // i, n) for i in range(1, m + 1))
        return result


f = FindKthSmallestNumber()
print(f.finding(3, 3, 5))
