class Solu:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        c1 = len(nums1)
        c2 = len(nums2)
        intersec = []
        if c1 > c2:
            for i in nums2:
                if i in nums1:
                    min_count = min(nums1.count(i), nums2.count(i))
                    while min_count > intersec.count(i):
                        intersec.append(i)
        else:
            for i in nums1:
                if i in nums2:
                    min_count = min(nums1.count(i), nums2.count(i))
                    while min_count > intersec.count(i):
                        intersec.append(i)


        return intersec


s = Solu()
l = s.intersect([1, 2, 2, 1], [2, 2])
for i in l:
    print(i, end=" ")
