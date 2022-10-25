class RomanNumber:
    num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def roman_int(self, s: str) -> int:
        left = 0
        right = 1
        n = len(s)
        window = ""
        total = 0
        while right < n:
            # if s[left] == s[right]:
            #     window += s[right]
            #     left += 1
            #     right += 1
            # elif self.num_dict[s[left]] < self.num_dict[s[right]]:
            #         window += s[right]
            #         left += 1
            #         right += 1
            # else:
            #     for c in window:
            if self.num_dict[s[left]] < self.num_dict[s[right]]:
                total = total + self.num_dict[s[right]] - self.num_dict[s[left]]
                left = right + 1
                right += 1
            elif self.num_dict[s[left]] == self.num_dict[s[right]]:
                if s[min(right + 1, len(s) - 1)] == 'I':
                    total += 1
                    right += 1
                total += 2
                left = right + 1
                right += 1
            elif self.num_dict[s[left]] > self.num_dict[s[right]]:
                total += self.num_dict[s[left]]
                left = right
                right += 1

        return total

    # 返回 1， 0， -1 分别表示 大于等于小于
    def compare(self, left, right) -> int:
        return 0


r = RomanNumber()
r.roman_int("MCMXCIV")
