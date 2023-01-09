class ShortBridge:
    def shortest_bridge(self, grid: [[int]]) -> int:
        # find an island
        n = len(grid)
        bridge_length = -1

        def find_whole_land(row: int, col: int):
            land_1.append([row, col])
            # check four direction
            if row - 1 >= 0 and grid[row - 1][col] and [row - 1, col] not in land_1:
                find_whole_land(row - 1, col)
            if col + 1 <= n - 1 and grid[row][col + 1] and [row, col + 1] not in land_1:
                find_whole_land(row, col + 1)
            if row + 1 <= n - 1 and grid[row + 1][col] and [row + 1, col] not in land_1:
                find_whole_land(row + 1, col)
            if col - 1 >= 0 and grid[row][col - 1] and [row, col - 1] not in land_1:
                find_whole_land(row, col - 1)
            pass

        land_1 = []
        found_island = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    # find this island
                    find_whole_land(i, j)
                    found_island = True
                    break
            if found_island:
                break
        # Now one island is found, next find the shortest bridge
        cost = 0  # the length of the bridge

        def BFS(temp_layer: [], cost: int):
            cost += 1
            next_layer = []
            found = False
            # find the outer layer
            for pos in temp_layer:
                # check if there's 0 in four directions: pos[0] -> i, pos[1] -> j
                # if pos[0] - 1 >= 0 and not grid[pos[0] - 1][pos[1]] and [pos[0] - 1, pos[1]] not in next_layer:
                #     next_layer.append([[pos[0] - 1], pos[1]])
                # if pos[1] + 1 <= n - 1 and not grid[pos[0]][pos[1] + 1] and [pos[0], pos[1] + 1] not in next_layer:
                #     next_layer.append([pos[0], pos[1] + 1])
                # if pos[0] + 1 <= n - 1 and not grid[pos[0] + 1][pos[1]] and [pos[0] + 1, pos[1]] not in next_layer:
                #     next_layer.append([pos[0] + 1, pos[1]])
                # if pos[1] - 1 >= 0 and not grid[pos[0]][pos[1] - 1] and [pos[0], pos[1] - 1] not in next_layer:
                #     next_layer.append([pos[0], pos[1] - 1])
                # UP
                if pos[0] - 1 >= 0 and [pos[0] - 1, pos[1]] not in temp_layer:
                    # if reached the island(is 1)
                    if grid[pos[0] - 1][pos[1]]:  # == 1
                        found = True
                        break
                    elif [pos[0] - 1, pos[1]] not in next_layer:  # grid[pos[0] - 1][pos[1]] == 0
                        next_layer.append([pos[0] - 1, pos[1]])
                # RIGHT
                if pos[1] + 1 <= n - 1 and [pos[0], pos[1] + 1] not in temp_layer:
                    if grid[pos[0]][pos[1] + 1]:
                        found = True
                        break
                    elif [pos[0], pos[1] + 1] not in next_layer:
                        next_layer.append([pos[0], pos[1] + 1])
                # DOWN
                if pos[0] + 1 <= n - 1 and [pos[0] + 1, pos[1]] not in temp_layer:
                    if grid[pos[0] + 1][pos[1]]:
                        found = True
                        break
                    elif [pos[0] + 1, pos[1]] not in next_layer:
                        next_layer.append([pos[0] + 1, pos[1]])
                # LEFT
                if pos[1] - 1 >= 0 and [pos[0], pos[1] - 1] not in temp_layer:
                    if grid[pos[0]][pos[1] - 1]:
                        found = True
                        break
                    elif [pos[0], pos[1] - 1] not in next_layer:
                        next_layer.append([pos[0], pos[1] - 1])
                # end finding
            pass
            if found:
                bridge_length = cost + 1
                return
            # else do next layer
            else:
                BFS(next_layer, cost)
            pass
        BFS(land_1, cost)
        return bridge_length


shor = ShortBridge()
print(shor.shortest_bridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
