class Slotion:
    def combine(self, n: int, k: int) -> [[int]]:
        def select_numbers(n: int, k: int) -> [[int]]:
            if n == 1:
                return [[1]]
            if k == n:
                return [x for x in range(1, n + 1)]
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
            return single_group

        return select_numbers(n, k)

c = Slotion()
print(c.combine(2, 2))