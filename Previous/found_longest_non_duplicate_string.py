# 给定一个字符串，请找出不含有重复字符的最长子串的长度
class Solution1:
    def length_of_longest_sub_string(self, s: str) -> int:
        # single = []
        # max_len = 0
        # for c in s:
        #     if single.count(c) == 0:
        #         single.append(c)
        #         if max_len < len(single):
        #             max_len = len(single)
        #     else:  # 此时是已经有该元素，那么删掉其本身和前面的所有元素
        #         # 需要单独处理两个字符挨在一起的情况
        #         if single[len(single) - 1] == c:
        #             single.clear()
        #             single.append(c)
        #         else:
        #             single = single[single.index(c) - 1:]
        #             single.append(c)
        #
        # print("Max Length: {0}".format(max_len))
        # return max_len
        window = []
        max_len = 0
        left = right = 0
        n = len(s)
        if s == "" or not s:
            return 0
        while right < n:
            if s[right] not in window:
                window.append(s[right])
                if max_len < len(window):
                    max_len = len(window)
                right += 1
            else:  # 此时 window 中含有 s[right]
                window = window[window.index(s[right]):]  # 左侧裁切
                window.remove(s[right])
                left = s.index(window[0])
                print("Max:" + str(max_len))
        return max_len




s1 = Solution1()

Solution1.length_of_longest_sub_string(s1, s="dvdf")

