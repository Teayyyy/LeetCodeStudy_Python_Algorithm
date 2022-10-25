class BestTimeToBuyAndSellStock:
    def best_time(self, prices: [int]) -> int:
        # 计算出天数的长度
        n = len(prices)
        # 用两个指针来指向当前一天和后一天，依次往后运行
        profit = 0  # 用来计算总的价格
        for i in range(n - 1):
            # 规划天数
            today = i
            tomorrow = i + 1
            profit += max(prices[tomorrow] - prices[today], 0)
        return profit


b = BestTimeToBuyAndSellStock()
print(b.best_time([7, 1, 5, 3, 6, 4]))
