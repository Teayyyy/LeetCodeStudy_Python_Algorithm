class maxProfit:
    max_n_profit = {}

    def max_profit(self, prices: [int]) -> int:
        for i in range(1, len(prices)):
            if i == 1:
                self.max_n_profit[i] = max(prices[i] - prices[0], 0)
            else:
                self.max_n_profit[i] = max(self.max_n_profit[i - 1], prices[i] - min(prices[:i - 1]))
        return max(self.max_n_profit.values())

    def max_profit_1(self, prices: [int]) -> int:
        n = len(prices)
        # 用来保存全剧最大
        max_price = 0
        for i in range(n):
            temp_max = 0 # 用来保存当前日期最大
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                temp_max = max(profit, temp_max)
            max_price = max(temp_max, max_price)
        return max_price





m = maxProfit()
# print(m.max_profit([7, 1, 5, 3, 6, 4]))
# print(m.max_profit([7, 1, 5, 3, 6, 4]))

print(m.max_profit([7,6,4,3,1]))
