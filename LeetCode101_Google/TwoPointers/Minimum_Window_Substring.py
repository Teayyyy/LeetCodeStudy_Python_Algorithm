from collections import defaultdict

class MinimumWindowSubstring:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if len(t) == 1 and len(s) == 1 and s == t:
            return t
        if s is t:
            return s
        # 对 t 进行数据统计
        count_t = {}
        for c in t:
            if c not in count_t:
                count_t[c] = 1
            else:
                count_t[c] += 1
        # 使用滑动窗口来进行计算
        # 使用两个指针，来设置不同的窗口
        former, latter = 0, 0  # 此时指向最小的滑动窗口
        min_len = 100000
        substr = ""
        while latter < len(s):
            # 判断当前的窗口内是否包含所有的字串
            if self.inside(count_t, s[former:latter + 1]):  # 如果包含
                temp_len = latter - former
                # 如果找到了更小的字串，那么更新
                if temp_len < min_len:
                    min_len = temp_len
                    substr = s[former: latter + 1]
                # 将former移动到下一个包含有 t 中字符到位置
                while True:
                    former += 1
                    if former >= len(s):
                        break
                    if s[former] in t:
                        latter -= 1
                        break
            latter += 1
        return substr

    @staticmethod
    def inside(count_t: {}, sub: str) -> bool:
        # 这里不仅要考虑到是否包含，还需要考虑到相同的字符也要再包含一次
        # 使用同样的方法来统计sub中的元素
        count_sub = {}
        for c in sub:
            if c not in count_sub:
                count_sub[c] = 1
            else:
                count_sub[c] += 1
        # TODO:统计完字符串后进行二者的比较
        for item in count_t:
            if item not in count_sub:
                return False
            elif count_t[item] > count_sub[item]:
                return False
        return True

    def minWindow_2(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if len(t) == 1 and len(s) == 1 and s == t:
            return t
        if s is t:
            return s
        # 对 t 进行数据统计
        count_t = {}
        need = 0  # 统计一共需要多少字符
        for c in t:
            if c not in count_t:
                count_t[c] = 1
            else:
                count_t[c] += 1
            need += 1
        former, latter = 0, 0
        answer = ""
        while latter < len(s):
            # 每个 latter 经过的字符都进行检验，是否在 count_t 中
            if s[latter] in count_t:
                count_t[s[latter]] -= 1
                if count_t[s[latter]] >= 0:
                    need -= 1
            # 移动 former
            if need == 0:
                if s[former] in count_t:  # 如果 former 指向的元素正好是在 t 中的
                    if not answer or len(answer) > latter - former:
                        answer = s[former: latter + 1]

            while need == 0:
                # if s[former] in count_t:  # 如果 former 指向的元素正好是在 t 中的
                #     if not answer or len(answer) > latter - former:  # 判断是否当前的字符串比原先的字符串更小
                #         answer = s[former: latter + 1]  # 更新 answer
                former += 1
                if s[former] in count_t:
                    if not answer or len(answer) > latter - former:
                        answer = s[former: latter + 1]  # 此时找到了目前字符串内最短的位置
                        # 接下来将 former 跃进到下一个包含在t中的字符上
                        need += 1
                        while s[former] not in count_t:
                            former += 1

            # 移动 latter
            latter += 1

        return answer

    def minWindow_3(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        hs, ht = defaultdict(int), defaultdict(int)  # 初始化新加入的 key 的 value 为 0
        for char in t:
            ht[char] += 1
        res = ""  # 用来储存结果
        left, right = 0, 0  # 滑动窗口
        cnt = 0  # 当前窗口中满足 ht 字符的个数
        while right < len(s):
            hs[s[right]] += 1  # 将当前这个元素的个数统计到 s 的哈希表中
            if hs[s[right]] <= ht[s[right]]:  # 这里成立说明，t中必须要s的这个元素
                cnt += 1  # 这个是用来计算当前滑动窗口中必须要包含的元素的个数
            while left < right and hs[s[left]] > ht[s[left]]:  # 当窗口内元素都符合要求的情况下压缩窗口
                # while 第二个条件表示的是：s中当前字符串的个数要多于t 中，这样才表明还有可压缩的空间，否则就是已经在当前情况下压缩到极限了
                hs[s[left]] -= 1
                left += 1
            if cnt == len(t):  # 当所必须的元素个数和t的长度相等时
                if not res or right - left + 1 < len(res):
                    res = s[left: right + 1]
            right += 1
        return res









m = MinimumWindowSubstring()
# print("Is: ", m.minWindow("ADOBECODEBANC", "ABC"))
print("Is: ", m.minWindow_3("cabbaa", "aba"))
