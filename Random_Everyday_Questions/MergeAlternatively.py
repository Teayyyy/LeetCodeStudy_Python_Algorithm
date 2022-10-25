class MergeAlternatively:
    def merge_alt(self, word1: str, word2: str) -> str:
        length = len(word1) if len(word1) <= len(word2) else len(word2)
        result = ""
        for i in range(length):
            result = result + word1[i] + word2[i]
        if length == len(word1):
            result += word2[length:]
            pass
        elif length == len(word2):
            result += word1[length:]
            pass
        return result

    def merge_2(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        length = l1 if l1 <= l2 else l2
        result = ""
        for i in range(length):
            result = result + word1[i] + word2[i]
        if length == l1:
            result += word2[length:]
        else:
            result += word1[length:]
        return result

    def merge_3(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        i = 0
        result = ""
        while True:
            result = result + word1[i] + word2[i]
            i += 1
            if i == l1:
                result += word2[i:]
                break
            elif i == l2:
                result += word1[i:]
                break

        return result



m1 = MergeAlternatively()
# print(m1.merge_alt(word1="abc", word2="pqr"))
print(m1.merge_3(word1="1234", word2="abcdeee"))
