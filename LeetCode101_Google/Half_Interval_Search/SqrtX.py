class SqrtX:
    def the_sqrt(self, x: int) -> int:
        # 这道题是求平凡根，采用二分查找的迭代法
        if x == 0:  # 对于 0 的情况，0 不能做除数
            return 0
        former, latter = 0, x  # 类似于双指针的做法，但是二分查找的指针移动速度更快，一次半个区间
        mid, sqrt = 0  # 构造情况：如果 mid * sqrt == x，则找到了，否则就用二分法继续往下寻找下去
        # 循环退出的情况是：左右指针不能相互超过（越界）
        while former <= latter:
            mid = int((former + latter) / 2)  # 这里没有像题中那样将 latter - 1
            sqrt = x // mid
            if sqrt == mid:
                return mid
            # 如果结果和mid相比，比较大，那么说明此时应该将 右指针减小
            elif mid > sqrt:
                latter = mid - 1
            # 如果此时结果和mid相比，比较小，那么说明此时应该将左指针增大
            elif mid < sqrt:
                former = mid + 1

        return latter

