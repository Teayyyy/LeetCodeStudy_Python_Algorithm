class Partition_Labels:
    def partionLabels(self, s: str) -> [int]:
        # 对字符串进行遍历，记录每个字母的信息
        info = []
        # 分别对26个字母进行配置信息
        for i in range(26):
            # 信息分别是：字母名称0、开始位置1、结束位置2、个数3，如果没有则为-1（默认值）
            info.append([chr(ord('a') + i), -1, -1, -1])

        # 遍历字符串进行信息的预处理
        count = 0  # 记录当前遍历到哪一个地方（指针)
        for c in s:
            # 记录开始位置
            pre = info[ord(c) - ord('a')]  # 获取之前的信息
            if pre[1] == -1:  # 如果当前字母没有被记录，那么说明第一次出现，则将当前的count记录到这里面
                pre[1] = count
                pre[3] = 1
            else:  # 如果当前字母首位已经有了记录，那么说明不是第一次出现，那么实时更新最后一次出现的位置，这样在所有遍历完成的时候每一个字母都记录到了最后一位的位置
                #  但是需要注意，如果在后面最后一位检测到 -1 的时候， 则检查出现个数
                pre[2] = count
                pre[3] += 1  # 更新个数
            info[ord(c) - ord('a')] = pre
            count += 1

        # 然后开始合并区间
        info.sort(key=lambda x: x[1] and x[1] != -1)
        print(info)

        # # 用来记录拆分字符串的位置
        # indexes = []
        #
        # # # 开始正式分裂字符串
        # # # 使用指针的方式来寻找
        # # now = 0  # 记录现在指针的位置，初始化为第一个字符的索引
        # # temp_end = info[0][2]  # 记录当前包含在字符串里最后的字母的位置
        # # while now < len(s):  # 设置循环退出的条件
        # #     # 如果下面条件达成，说明找完了一个字符串片段
        # #     pass
        # #     if now == temp_end:
        # #         # 记录当前这一段字符串
        # #         indexes.append(now)
        # #         # 开始下一步的查找
        # #         now = temp_end + 1
        # #         continue
        # #     # 没有查找完一个目标字符串的操作
        # #     else:
        # #         cha = info[ord(s[now]) - ord('a')]  # 获取当前字母的信息
        # #         if cha[3] == 1:
        # #             indexes.append(now)
        # #             now = temp_end + 1
        # #             continue
        # #         #
        # #         # if cha[2] + now > temp_end and cha[0] != s[now]:  # 如果字符不是当前最后一位的字符且最后一位大于此时的字符串末尾，则更新末尾
        # #         #     temp_end = cha[2] + now
        # #         # now += 1  # 更新当前指示字符串的指针
        # #         last_index = max(cha[1], cha[2])  # 获取最后一位的位置
        # #         if temp_end < last_index:
        # #             temp_end = last_index
        # #         now += 1
        #
        #
        # # 此时result中保存的是每个字符串的索引，需要再进行一次长度计算
        # # result = []
        # # for i in range(len(indexes)):
        # #     if i == 0:
        # #         result.append(indexes[i] + 1)
        # #     else:
        # #         result.append(indexes[i] - indexes[i - 1])

        # return result

    def partionLabels_2(self, s: str) -> [int]:
        # 对字符串进行遍历，记录每个字母的信息
        info = []
        # 分别对26个字母进行配置信息
        for i in range(26):
            # 信息分别是：字母名称0、开始位置1、结束位置2、个数3，如果没有则为-1（默认值）
            info.append([-1, -1])  # 排序方式按照字母顺序，索引为 ASCII码

        for i in range(len(s)):
            ind = ord(s[i]) - ord('a')  # 获取 ASCII 索引
            if info[ind][0] == -1:  # 没有初始位，则赋值
                info[ind][0] = i
            elif info[ind][1] < i:  # 有初始位，则赋末尾值
                info[ind][1] = i
        # 清除掉info中空的数据，处理末尾索引为-1的数据
        processed = []
        for i in info:
            if i[0] != -1:
                if i[1] != -1:
                    processed.append(i)
                else:
                    processed.append([i[0], i[0]])

        # 按照字母的起始位置进行排序
        processed.sort(key=lambda x: x[0])

        print("Proceed:", processed)
        # 对字母区间进行合并
        result = []
        # TODO: 查找合并区间的方法
        result = self.mergeRange(processed)

        return result

    def mergeRange(self, processed):
        # 记录每段字符串的起始结束位置
        start = end = 0
        # 记录位置的地方
        index = []
        for i in processed:
            front, rear = i[0], i[1]
            if end < front:
                index.append(end - start + 1)  # 记录这段字符串的长度
                start = front
            end = max(end, rear)
        # 单独处理最后一个
        index.append(end - start + 1)

        return index



p = Partition_Labels()
# print(p.partionLabels_2('accabbd'))
print(p.partionLabels_2("ababcbacadefegdehijhklij"))
