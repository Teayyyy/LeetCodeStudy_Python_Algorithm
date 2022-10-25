class Combinations:
    def combine(self, n: int, k: int) -> [[int]]:
        '''
        To finish this, we need to split the big question into several smaller one:
        1. select k numbers in range of [1,n], called temp_group
        2. process all the possible combinations of temp_group
        '''

        # Step 1: select K numbers in range [1, n]
        def select_numbers(n: int, k: int) -> [[int]]:
            # Using recursion
            numbers = [j for j in range(1, n + 1)]  # make the list ranges in [1, n]
            groups = []

            def select_dfs(temp_group: [int]):
                for i in range(len(numbers)):
                    if len(temp_group) == k:
                        groups.append(temp_group[:])
                        return
                    if numbers[i] not in temp_group:
                        temp_group.append(numbers[i])
                        select_dfs(temp_group[:])
                        temp_group.pop(len(temp_group) - 1)
                pass

            for i in range(len(numbers)):
                temp = [numbers[i]]
                select_dfs(temp[:])

            print("Step one finished! Results are listed below: ")
            # purify groups to single element exists in
            single_group = []
            for item in groups:
                item.sort()
                if item not in single_group:
                    single_group.append(item)
            # print("Groups:")
            # for item in groups:
            #     print(item, end=", ")
            # print("\nSingle Groups: ")
            # for item in single_group:
            #     print(item, end=", ")
            # print("*" * 30)
            return single_group

        return select_numbers(n, k)

    def select_number_2(self, n: int, k: int) -> [[int]]:
        begin = 0
        path = []
        result = []
        def DFS(begin: int, path: [int]):
            for i in range(begin, n + 1):
                # if n + 1 + len(path) - k >= i:
                #     return
                if len(path) == k:
                    result.append(path)
                    return
                # path.append(i + 1)
                DFS(i + 1, path[:] + [i + 1])

        DFS(begin, path[:])
        return result

c = Combinations()
# print(c.combine(2, 2))
print(c.select_number_2(4, 2))
print("All finished!")
