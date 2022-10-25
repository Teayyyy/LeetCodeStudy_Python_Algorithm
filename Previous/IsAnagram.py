class IsAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        # 首先比较长度
        if len(s) != len(t):
            return False
        l1, l2 = [0 for i in range(26)], [0 for i in range(26)]
        print(l1, l2, end="\n")
        for i in range(len(s)):
            l1[ord(s[i]) - ord('a')] += 1
            l2[ord(t[i]) - ord('a')] += 1
        print(l1, l2, end="\n")
        for i in range(26):
            if l1[i] != l2[i]:
                return False
        return True

iss = IsAnagram()
print(iss.isAnagram("rat", "car"))