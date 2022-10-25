class Candy:
    def candy(self, ratings: [int]) -> int:
        n = len(ratings)
        count = 0
        current = 1
        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                current += 1
                count += current
            elif ratings[i] >= ratings[i + 1]:
                # 如果出现了较小于当前的，那么继续向后找知道出现第一个增加
                skip = 0
                while True:
                    # 设置推出循环条件，超出范围了仍然要计算
                    if i + skip >= n - 1:
                        # for j in range(skip + 1):
                        # count += skip
                        # if skip > 1:
                        #     skip += 1
                        if skip >= n - i - 1:
                            for j in range(skip + 1):
                                count += skip
                                if skip > 1:
                                    skip -= 1
                        else:
                            for j in range(skip + 1):
                                count += j
                        break
                    # 当下一个元素仍然成非增长时，继续往后寻找
                    if ratings[i + skip] >= ratings[i + skip + 1]:
                        skip += 1
                    # 当找到了第一个开始增长的元素时，则从1 开始递增的加skip次，同时退出循环
                    else:
                        for j in range(skip + 1):
                            count += j

                        i += skip  # 将i跳到第一个增加的位置
                        current = 1  # 重制 current，因为要保证分配的最少
                        break
        # 特殊处理最后一个
        if ratings[n - 2] < ratings[n - 1]:
            count += current
        else:
            count += 1
        print(ratings)
        return count

    def candy2(self, ratings: [int]) -> int:
        n = len(ratings)
        count = 0
        current = 1
        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                current += 1
                count += current
            elif ratings[i] >= ratings[i + 1]:
                # 在出现了下降的趋势时候，应该考虑的情况：
                # 画图解析，有思路但是不知道怎么实现
                skip = 0
                while True:
                    # TODO
                    pass
        # 单独处理最后一个
        return 0


    def candy3(self, ratings: [int]) -> int:
        # 通过例题的讲解，得到一下算法：
        n = len(ratings)
        candy_list = [1 for i in range(n)]
        for i in range(1, n):
            # 此时只要左边分数小于右边分数，那么右边的糖果数就需要比左边的糖果数多1个
            if ratings[i] > ratings[i - 1]:
                candy_list[i] = candy_list[i - 1] + 1
        for i in range(1, n):
            # 这里不仅要判断是否 n - i 的得分比 n - i - 1 的小，同时还要看前者的糖果数是否已经符合要求了，因为要求的是分发最少的糖果数，所以非必要不发糖
            if ratings[n - i] < ratings[n - i - 1] and candy_list[n - i] >= candy_list[n - i - 1]:
                candy_list[n - i - 1]  = candy_list[n - i] + 1
        sum = 0
        for i in candy_list:
            sum += i
        return sum




c = Candy()
try1 = [1, 2, 2]
try2 = [1, 3, 2, 2, 1]
# print(c.candy(try2))
c.candy3(try2)