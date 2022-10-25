class solution:
    types = 0

    def climb_stairs(n: int) -> int:
        if n == 1:
            return 1
        count = 0
        ns = n // 2
        if n % 2:
            return 1 + 2 ** ns
        else:
            return 2 ** ns

    def climb_stairs_2(self, n: int) -> int:
        self.types = 0

        def climb_next(temp_stairs: int):
            print(self.types)
            if temp_stairs >= n:
                self.types += 1
                return
            elif (n - temp_stairs) >= 2:
                climb_next(temp_stairs + 1)
                climb_next(temp_stairs + 2)
            else:
                climb_next(temp_stairs + 1)
            pass

        climb_next(0)
        return self.types

    def climb_official(self, n: int) -> int:
        # this is so called dynamic programming
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        i = 2
        while i <= n:
            print(i)
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1
        return dp[n]


s = solution()
# print("this", s.climb_stairs_2(10))
print("this time:", s.climb_official(38))
