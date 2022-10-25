# 射出箭射爆气球的最少数
class MinimumNumberOfArrows:
    def minimum_number_of_arrow(self, points: [[int]]) -> int:
        # 对气球进行排序，排序的方法为：按照直径的从小到大进行排序
        points.sort(key=lambda x: x[1] - x[0])
        arrow = 0  # 射出的箭数
        for balloon in points:
            # 首先这个气球被射爆了
            points.pop(0)
            arrow += 1
            # 查找交集
            union = set(balloon)
            # for another_balloon in points:
            #     # 取交集
            #     temp = list(set(union) & set(another_balloon))
            #     # 如果两者是空集，则说明这个气球无法被射爆，那么开始看下一个
            #     if temp == []:
            #         continue
            #     # 如果存在交集，那么这个说明这个气球也可以被射爆
            #     else:
            #         union = temp
            #         # 射爆气球
            #         points.pop(points.index(another_balloon))
            pop_list = []  # 考虑到循环，采用循环完成后爆炸的思想
            for i in range(len(points)):
                temp = list(set(union) & set(points[i]))
                if temp == []:
                    continue
                else:
                    union = temp
                    pop_list.append(i)
            for pops in pop_list:
                points.pop(pops)
        return arrow

    def minimum_number_of_arrows_2(self, points: [[int]]) -> int:
        # 进行排序
        points.sort(key=lambda x: x[1] - x[0])  # 这个是按照最小的气球直径进行排序
        arrow = 0
        while points:
            # 获得第一个气球
            balloon = points[0]
            # 首先射爆第一个气球
            points.pop(0)
            arrow += 1
            # 查找还有没有气球可以被射爆，实质上就是在寻找交集
            # union = set(balloon)
            union = balloon
            # 开始逐个查找其他气球是否能够同时被射爆
            pop_list = []  # 用来缓存爆炸的气球
            for i in range(len(points)):
                # 取交集 这里需要重新写一个函数
                # temp = list(set(union) & set(points[i]))
                temp = self.get_union_range(union, points[i])
                if not temp:
                    continue
                else:
                    union = temp
                    pop_list.append(i)
                # 这里删除操作好实现，因为数组现在呈现动态变化
            points = [points[i] for i in range(len(points)) if (i not in pop_list)]

        return arrow

    # 将获取到的数组找到其交集部分[a, c], [b, d] [1, 3] [2, 4]
    def get_union_range(self, l1: [int], l2: [int]) -> [int]:
        # 需要默认 l1 l2 按照第一个元素增序的方式排列
        if l1[0] > l2[0]:
            l1, l2 = l2, l1
        if l2[0] > l1[1]:
            return []
        else:
            return [max(l1[0], l2[0]), min(l1[1], l2[1])]

    # 新的方法！！！！！！类似于热点图
    def new_minimum_arrow_shots(self, points: [[int]]) -> int:
        # 设置 10001 为了直接映射，减少错误发生
        hot_map = [0 for i in range(10 ** 5 + 1)]
        # 将每个气球覆盖的位置写在 hot map 上
        for balloon in points:
            for i in range(balloon[0], balloon[1] + 1):
                hot_map[i] += 1
        print(hot_map[: 20])

        return 0

    # 根据 leetcode 题解改进的方法
    def minimum_arrow_shots_3(self, points: [[int]]) -> int:
        # 气球按照起点位置进行排序
        points.sort(key=lambda x: x[0])
        print(points)
        arrow = 0
        # 逐个射爆
        while points:
            balloon = points.pop(0)
            arrow += 1

            union_range = balloon
            pop_list = []  # 用来记录当前循环中要爆炸对气球
            # count = 0
            # for i in range(len(points)):
            #     temp = self.get_union_range(union_range, points[i])
            #     # count = i
            #     if not temp:  # 如果已经没有交集了，那么说明后面也不会有，因此直接爆掉气球进行下一轮循环
            #         break
            #     else:
            #         union_range = temp
            #         pop_list.append(i)
            while points:
                temp = self.get_union_range(union_range, points[0])
                if not temp:
                    break
                else:
                    union_range = temp
                    points.pop(0)
            # points = [points[j] for j in range(len(points)) if (j not in pop_list)]  # 这一步表示将前一段筛完成后加上后一段
            # points = [points[j] for j in range(count) if (j not in pop_list[:count + 1])] + points[count + 1:]

        return arrow

    def officical_solotion(self, points: [[int]]) -> int:
        if not points:
            return 0
        # 按照右侧距离进行检查
        points.sort(key=lambda x: x[1])
        arrow = 1
        pos = points[0][1]
        for balloon in points:
            if pos < balloon[0]:
                pos = balloon[1]
                arrow += 1
        return arrow


m = MinimumNumberOfArrows()
print(m.officical_solotion([[10, 16], [2, 8], [1, 6], [7, 12]]))
