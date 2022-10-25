# buildings = [[0, 2, 3], [2, 5, 3], [3, 7, 15], [5, 12, 12]]
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]


def get_silhouette(buildings):
    # TODO: 对建筑进行位置排序
    new_buildings = buildings
    final_silhouette = []
    # 判断哪些建筑是连接在一块
    merged_buildings = find_merges(new_buildings)  # 得到了连接在一起的建筑
    # 分组更改
    for building_group in merged_buildings:
        temp_silhouette = merge(building_group)
        final_silhouette.append([temp_silhouette])

    print("最终轮廓：", end="")
    for item in final_silhouette:
        print(item, end=" ")
    print()
    # print(merged_buildings)


def merge(group):
    # 这一组建筑的坐标
    silhouette = []
    # 分别获取长宽高最大值，找到边缘最大的矩形
    max_l = group[0][0]
    max_r = get_max(group, 1)
    max_h = get_max(group, 2)
    print("Maxes: L: {0}, R:{1}, H:{2}".format(max_l, max_r, max_h))
    # 对每个建筑的左右点进行判断
    for building in group:
        # 分别对三个值进行判断
        left, right, height = building[0], building[1], building[2]
        if height == max_h:  # 高度是最高的，直接加进两个点
            silhouette.append([left, height])
            silhouette.append([right, height])
        elif left == max_l:
            silhouette.append([left, height])
        elif right == max_r:
            silhouette.append([right, height])
    # END FOR 现在获得了所有在外的建筑点，但是没有计算建筑之间的交点
    print("在外的建筑点：", end="")
    for i in silhouette:
        print(i, end=" ")
    print()

    silhouette = find_intersections(silhouette)

    return silhouette


def find_intersections(points):
    temp_silhouette = []
    former, latter = 0, 1
    while latter < len(points):
        # 高度相同不要
        if points[former][1] == points[latter][1]:
            former += 1
            latter += 1
            continue
        # 找到较高的点
        if points[former][1] < points[latter][1]:
            temp_point = [points[latter][0], points[former][1]]
            temp_silhouette.append(temp_point)
        if points[former][1] > points[latter][1]:
            temp_point = [points[former][0], points[latter][1]]
            temp_silhouette.append(temp_point)
        former += 1
        latter += 1
    # 融合两个列表
    final_silhouette = []
    final_silhouette = temp_silhouette + points
    final_silhouette.sort()
    return final_silhouette



    # return temp_silhouette


def get_max(group, index):
    max = -1
    # 找到最大值
    for i in range(len(group)):
        if group[i][index] > max:
            max = group[i][index]
    return max


def find_merges(buildings):
    former, latter = 0, 1
    merge_buildings = []
    while former < len(buildings):
        # 当前组建筑
        temp_merge = []
        # 先将左侧放进去
        temp_merge.append(buildings[former])
        # 获取左右坐标
        former_right = buildings[former][1]
        # 当前一个建筑右侧比后一建筑的左侧更靠右，说明在内部
        while latter < len(buildings) and former_right > buildings[latter][0]:
            # 放入右侧建筑
            temp_merge.append(buildings[latter])
            # 移动到下一个建筑
            latter += 1

        # 到这里时说明后面没有能够和former合并的建筑，因此这里直接跳到 latter 上并且 latter 加一
        merge_buildings.append(temp_merge)  # 将这一组建筑放到列表组中
        print("Temp Merge: ", end="")
        for i in temp_merge:
            print(i, end=" ")
        print()
        former = latter
        latter += 1
        # END WHILE
    # END WHILE
    return merge_buildings


def main():
    get_silhouette(buildings)


main()
