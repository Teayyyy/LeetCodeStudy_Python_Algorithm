class QueueReconstructionByHeight:
    def queue_reconstruction(self, people: [[int]]) -> [[int]]:
        # 将 people 按照 前方有按照要求人数的从小到大的顺序进行排列
        # 在排序后，能够保证排序后的队列，每一个元素前面都是大于或者等于他的元素，这样在后续插入时能简化不少，即使是相等的元素之间，其元素对的第二个值（有多少个高于自己的人）也是按照升序排列的
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people)
        result = []
        # 按照要求插入的方法：当前已经插入的元素一定大于等于后面的元素，因此当前插入的元素，只需要考虑前面需要有多少个大于或等于的元素即可
        for p in people:
            if len(result) <= p[1]:
                result.append(p)
            elif len(result) > p[1]:
                result.insert(p[1], p)
        print(result)
        return result






q = QueueReconstructionByHeight()
q.queue_reconstruction([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])

