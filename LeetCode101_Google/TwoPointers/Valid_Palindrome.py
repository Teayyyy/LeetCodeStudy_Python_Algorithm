class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        # 验证是否是回文字符串，仍然适用双指针的写法
        # 记录头尾的位置
        latter = len(s) - 1
        if latter + 1 == 1:
            return True
        former = 0
        while former < latter:  # 正中间那一个不用验证，因为一个字符一定是回文串
            # 这里只判断英文字符，因此别的符号应该跳过
            while not s[former].isalpha():
                former += 1
            while not s[latter].isalpha():
                latter -= 1
            if s[latter].lower() != s[former].lower():
                return False
            former += 1
            latter -= 1
        return True

    def is_fucking_palindrome(self, s: str) -> bool:
        # 预处理字符串
        n = len(s) - 1
        # s = s.upper()
        pure_s = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                pure_s += c
        pure_s = pure_s.lower()
        print(pure_s)
        # 正式判断字符串
        n = len(pure_s)
        if n == 0:
            return True
        if n == 1:
            return True

        former = 0
        latter = n - 1
        while former < latter:
            if pure_s[former] != pure_s[latter]:
                return False
            former += 1
            latter -= 1
        return True

    def is_FUCKING_palindrome(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        if n == 1 and (s.isalpha() or s.isdigit()):
            return True
        former = 0
        latter = n - 1
        has_alpha = False
        while former < latter:
            while not s[former].isalpha() and not s[former].isdigit():
                former += 1
            while not s[latter].isalpha() and not s[latter].isdigit():
                latter -= 1
            if s[former] != s[latter]:
                if s[former].isdigit() or s[latter].isdigit():
                    return False
                if s[former].upper() != s[latter].upper():
                    return False
            if s[former].isalpha():
                has_alpha = True
            former += 1
            latter -= 1

        if not has_alpha:
            return False
        else:
            return True




v = ValidPalindrome()
# print(v.isPalindrome("A man, a plan, a canal: Panama"))
# print(v.isPalindrome("a."))
# print(v.is_fucking_palindrome("0P"))
# print(v.is_fucking_palindrome("0P"))
print(v.is_FUCKING_palindrome(""))
# print(v.is_FUCKING_palindrome("0P"))