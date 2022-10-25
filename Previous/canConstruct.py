class Solutionss:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list1 = [0 for x in range(26)]
        list2 = [0 for x in range(26)]
        for c in ransomNote:
            list1[ord(c) - ord('a')] += 1
        for c in magazine:
            list2[ord(c) - ord('a')] += 1

        print(list1)
        print(list2)

        for i in range(26):
            if list1[i] > list2[i]:
                return False

        return True




ss = Solutionss()
print(ss.canConstruct("aa", "ab"))