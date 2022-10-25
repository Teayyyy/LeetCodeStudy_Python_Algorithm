class PossibleBiPartition:
    def possible_way(self, n: int, dislikes: [[int]]) -> bool:
        # a polar array, each one should have only one side, True or False
        polar = [-1] * (n + 1)
        print(polar)
        # process the dislikes
        for couple in dislikes:
            # if first one is 0, means it is not grouped
            if polar[couple[0]] == -1 and polar[couple[1]] == -1:
                polar[couple[0]] = True
                polar[couple[1]] = False
                continue
            # couple[0]
            if polar[couple[0]] == -1:
                if polar[couple[1]]:
                    polar[couple[0]] = False
                elif not polar[couple[1]]:
                    polar[couple[0]] = True
                continue
            elif polar[couple[0]]:
                if polar[couple[1]]:
                    return False
                else:
                    polar[couple[1]] = False
                    continue
            elif not polar[couple[0]]:
                if not polar[couple[1]]:
                    return False
                else:
                    polar[couple[1]] = True
                    continue
            # couple[1]
            if polar[couple[1]] == -1:
                if polar[couple[0]]:
                    polar[couple[1]] = False
                elif not polar[couple[0]]:
                    polar[couple[1]] = True
                continue
            elif polar[couple[1]]:
                if polar[couple[0]]:
                    return False
                else:
                    polar[couple[0]] = False
                    continue
            elif not polar[couple[1]]:
                if not polar[couple[0]]:
                    return False
                else:
                    polar[couple[0]] = True
                    continue
            pass
        print(polar)
        return True

    def possible_way_2(self, n: int, dislikes: [[int]]) -> bool:
        # sort dislike
        dislikes.sort(key=lambda x: x[0])
        print(dislikes)
        # RULE: no-touched: 0  True: 1  False: -1
        polar = [0] * (n + 1)
        print(polar)

        for couple in dislikes:
            if polar[couple[0]] == 0 and polar[couple[1]] == 0:
                polar[couple[0]] = 1
                polar[couple[1]] = -1
                continue  # Always remember to jump into another iteration when all operations finished.
            # couple[0]
            if polar[couple[0]] == 0:
                if polar[couple[1]] == 1:
                    polar[couple[0]] = -1
                elif polar[couple[1]] == -1:
                    polar[couple[0]] = 1
                continue
            elif polar[couple[0]] == 1:
                if polar[couple[1]] == 1:
                    return False
                else:
                    polar[couple[1]] = -1
                    continue
            elif polar[couple[0]] == -1:
                if polar[couple[1]] == -1:
                    return False
                else:
                    polar[couple[1]] = 1
                    continue
            # couple[1]
            if polar[couple[1]] == 0:
                if polar[couple[0]] == 1:
                    polar[couple[1]] = -1
                elif polar[couple[0]] == -1:
                    polar[couple[1]] = 1
                continue
            elif polar[couple[1]] == 1:
                if polar[couple[0]] == 1:
                    return False
                else:
                    polar[couple[0]] = -1
                    continue
            elif polar[couple[1]] == -1:
                if polar[couple[0]] == -1:
                    return False
                else:
                    polar[couple[0]] = 1
                    continue
        return True

    def possible_way_3(self, n: int, dislikes: [[int]]) -> bool:
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        color = [0] * n

        def DFS(x: int, c: int) -> bool:
            color[x] = c
            return all(color[y] != c and (color[y] or DFS(y, -c)) for y in g[x])

        return all(c or DFS(i, 1) for i, c in enumerate(color))



p = PossibleBiPartition()
# print(p.possible_way_3(4, [[1, 2], [1, 3], [2, 4]]))
print(p.possible_way_3(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
# print(p.possible_way_3(10, [[1, 2], [3, 4], [5, 6], [6, 7], [8, 9], [7, 8]]))
