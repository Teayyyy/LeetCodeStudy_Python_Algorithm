class IsPrefixOfWord:
    def is_prefix(self, sentence: [str], searchWord: str) -> int:
        '''
        如果 searchWord 是某一个单词的前缀，那么返回句子在该单词所对应的下标（从 1 开始）
        如果是多个单词的前缀，那么返回匹配的第一个单词的下标（最小下标）
        如果不是任何单词的前缀，那么返回 -1
        '''
        # split sentence to words in array
        word_list = sentence.split(" ")
        for word in word_list:
            is_finish = True
            if len(word) < len(searchWord):
                continue
            for i in range(len(searchWord)):
                if word[i] is not searchWord[i]:
                    is_finish = False
                    break
            if is_finish:
                return word_list.index(word) + 1
        return -1


isp = IsPrefixOfWord()
# print(isp.is_prefix("this problem is an easy problem", "pro"))
print(isp.is_prefix("i love eating burger", "burg"))
