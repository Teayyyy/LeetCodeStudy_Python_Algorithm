def firstUniqChar(s: str) -> int:
    # 字符计数
    alphabet = [0 for i in range(26)]
    for c in s:
        alphabet[ord(c) - 1 - ord('a')] += 1
    # 这里不是全部按照字母表顺序遍历，而是按照 s 的顺比来遍历
    for c in s:
        if alphabet[ord(c) - 1 - ord('a')] == 1:
            return s.index(c)


print(firstUniqChar("aleetcode"))