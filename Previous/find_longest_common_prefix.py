class FindLongestCommonPrefix:
    def longestCommonPrefix(self, strs: [str]) -> str:
        prefix = ""
        if len(strs) == 1:
            return strs[0]
        # 找到最小的字符串
        min_len = 0
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            is_same = True
            print(str(i) + " Comparing ***********")
            for s in strs:
                print(strs[0][:i])
                is_same = s.startswith(strs[0][:i + 1]) and is_same
                print(is_same)
            if is_same:
                prefix += strs[0][i]
                print("Add: " + strs[0][i])

        return prefix

    def longest(self, strs: [str]) -> str:
        if not strs: return ""
        s1 = min(strs)
        print(s1)
        s2 = max(strs)

        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
            return s1


f = FindLongestCommonPrefix()
# sub = f.longestCommonPrefix(["flower", "flow", "flight"])
sub = f.longest(["flower", "flow", "flight"])
print(sub)
