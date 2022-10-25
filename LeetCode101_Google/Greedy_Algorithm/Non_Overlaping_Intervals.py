# This is a medium-level
# 如何对数组中特定的元素进行排序？
class NonOverLappingInterval:
    # 默认返回第二个元素作为排序的对象
    def find_second(self, this_list: [int]) -> int:
        return this_list[1]


    def solution(self, inputs: [[int]]) -> int:
        # 首先对输入的数组进行排序，顺序是按照第二个元素来进行排序
        inputs.sort(key=self.find_second)
        # 另一种写法
        # inputs.sort(key=lambda x: x[1])
        # 逐个查找
        n = len(inputs)
        pre = 0
        count = 0
        for i in range(1, n):
            if inputs[i][0] >= inputs[pre][1]:
                pre = i
            else:
                count += 1
        return count


n = NonOverLappingInterval()

print(n.solution([[1, 2], [2, 4], [1, 3]]))
