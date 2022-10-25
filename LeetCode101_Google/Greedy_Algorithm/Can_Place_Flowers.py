class CanPlaceFlowers:
    def can_place_flowers(self, flowerbed: [int], n: int) -> bool:
        num = len(flowerbed)
        if num == 1 and n > 1:
            return False
        count = 0
        i = 0
        while i < num:
            # 专门考虑最后一位的情况
            if i == num - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    count += 1
                    break
                else:
                    break
            if flowerbed[i] == 1:
                i += 2
            elif flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
                i += 2
            else:
                i += 2

        print(count)
        if count >= n:
            return True
        else:
            return False

    def canPlace(self, flowerbed: [int], n: int) -> bool:
        num = len(flowerbed)

        # 单独处理1个元素的时候
        if num == 1:
            if flowerbed[0] == 0:
                return True
            elif flowerbed[0] == 1 and n == 0:
                return True
            else:
                return False

        count = 0
        for i in range(num):
            # 单独考虑几个点位的特殊情况
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
                    # 为什么这里要 += 1？
                    #   因为当前位置如果种了花，那么下一位一定不能种花保持空的位置，这样才能继续种花，因此直接移动两位，又因为python每次循
                    #   环结束后，i 会自动加 1，因此这里只需要再给 i + 1 即可满足跳两位的需求
                    i += 1
            elif i == num - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    count += 1
            else:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
                    i += 1
        if count >= n:
            return True
        else:
            return False


c = CanPlaceFlowers()
# print(c.can_place_flowers([1, 0, 0, 0, 1, 0, 0], 2))

print(c.canPlace([1, 0, 0, 0, 1, 0, 0], 2))
