class majorityElement:
    def majorityelement(self, nums):
        check_list = [0 for i in range(5 * 10 ** 4 + 1)]
        for i in nums:
            check_list[i] += 1
        return check_list.index(max(check_list))


m = majorityElement()
print(m.majorityelement([1, 1, 1, 2, 3]))