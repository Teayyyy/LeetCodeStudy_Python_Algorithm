class ConvertS2I:
    def myAtoi(self, s: str) -> int:
        symbol = 1
        total = 0
        last = ""
        for c in s:
            if c == '-' and symbol is not -1:
                symbol = -1
            # elif c.isnumeric() and last.isnumeric():
            elif c.isnumeric():
                total *= 10
                total += int(c)
                last = c
        return total * symbol

    def newAtoI(self, s: str) -> int:
        # 去掉空格
        s2 = ""
        symbol = 1
        total = 0
        for c in s:
            if c == " ":
                continue
            else:
                if c == '-':
                    symbol = -1
                elif not c.isnumeric():
                    break
                elif c.isnumeric():
                    total *= 10
                    total += int(c)
        # 检测是否超过
        total = symbol * total
        if total < -2 ** 31:
            return -2**31
        elif total > 2 ** 31:
            return 2 ** 31
        else:
            return total

        # print(s2)

    def newnewAtoI(self, s: str) -> int:
        length = len(s)
        symbol = 1
        total = 0
        left = 0
        next = 0
        # 找到第一个不是空格的地方
        for c in s:
            if c == " ":
                left += 1
            else:
                next = left + 1
                break

        if s[left].isalpha():
            return 0

        while left < length:
            if s[left] == "-" and s[next].isnumeric():
                symbol = -1
            elif s[left].isnumeric():
                if next >= length:
                    total *= 10
                    total += int(s[left])
                    break
                if s[next].isnumeric() or s[next] == " ":
                    total *= 10
                    total += int(s[left])
                elif s[next].isalpha():
                    return 0
            left = next
            next += 1

        total = symbol * total
        if total < -2 ** 31:
            return -2 ** 31
        elif total > 2 ** 31:
            return 2 ** 31
        else:
            return total




s = ConvertS2I()
# print(s.myAtoi("   -42"))
# print(s.newAtoI("   -42"))
# print(s.newnewAtoI("-91283472332"))
# print(s.newnewAtoI("00000-42a1234"))
print(s.newnewAtoI("3.14159"))