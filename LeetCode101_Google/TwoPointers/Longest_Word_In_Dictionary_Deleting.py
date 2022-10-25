class LongestWordInDictionaryDeleting:
    def findLongestWord(self, s: str, dictionary: [str]) -> str:
        # 将 dictionary 转换成字典，将初始值设置成0
        new_dict = {}
        for item in dictionary:
            new_dict[item] = 0
        # 计算字符的数量
        for c in s:
            print(c, end="")
            for item in new_dict:
                if new_dict[item] < len(item) and c is item[new_dict[item]]:
                    new_dict[item] += 1
        print(new_dict)
        max_len = 0
        the_str = ""
        for item in new_dict:
            if new_dict[item] == len(item):
                if max_len < len(item):
                    max_len = len(item)
                    the_str = item
                # 判断两个字符串中字符序更小的那一个
                elif max_len == len(item):
                    # for i in range(max_len):
                    #     if item[i] < the_str[i]:
                    #         the_str = item
                    #         break
                    # for i in range(max_len):
                    #     if the_str[i] == item[i]:
                    #         continue
                    #     elif the_str[i] > item[i]:
                    #         the_str = item
                    #         break
                    if the_str > item:
                        the_str = item

        return the_str


l = LongestWordInDictionaryDeleting()
# print(l.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
# print(l.findLongestWord("abce", ["abe", "abc"]))
print(l.findLongestWord("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
