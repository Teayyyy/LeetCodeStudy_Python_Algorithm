import math
class SumOfTwoNumbers:
    def sum_numbers(self, c: int) -> bool:
        # 这道题是 Two Sum 的变形之一，因此这道题仍然使用双指针方法来做
        former = 0
        # 记住这个操作
        latter = math.sqrt(c)
        while former <= latter:
            answer = former * former + latter * latter
            # 这会儿判断 answer 的大小
            if answer == c:
                return True
            elif answer > c:
                latter -= 1
            elif answer < c:
                former += 1
        return False

s = SumOfTwoNumbers()
print(s.sum_numbers(1))