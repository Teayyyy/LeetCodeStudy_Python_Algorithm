class TheKthGrammarSymbol:
    def kth_grammar(self, n: int, k: int) -> int:
        result = [False]
        # make it to the nth line:
        for i in range(n):
            result = result + [not j for j in result]
        print(result)
        return 1 if result[k - 1] else 0

    def kth_2(self, n: int, k: int) -> int:
        result = "01101001"
        if n > 3:
            for i in range(3, n):
                result = result + result[::-1]
        print(result)
        return int(result[k - 1])

    def kth_3(self, n: int, k: int) -> int:
        strings = "01101001"
        two_strings_move = k % (2 * len(strings))
        # strings = strings + strings[::-1]
        strings += "10010110"
        if (k // len(strings)) % 2 == 1:
            strings = "1001011001101001"

        return int(strings[two_strings_move - 1])

    def kth_3_recursive(self, n: int, k: int) -> int:
        '''
        This method is about the recursion, if we want to find its 0 or 1 in level n and the kth, we need to
        find the upper level (level - 1), its parent, and recursively find its father till we reach the end,
        and the root is always 0, so the whole recursion is completed.
        '''

        # level saves which layer now, if it reaches 1, means we reaches the root.
        level = k

        # The recursive function
        def recur_to_top(temp_layer: int, temp_loc: int):
            # temp_layer: current layer
            # temp_loc: current location
            # how to escape from recurse?
            if temp_layer == 1:
                return 0
            else:
                if temp_loc % 2 == 0:
                    pre_loc = temp_loc // 2
                else:
                    pre_loc = (temp_loc + 1) // 2
                last_num = recur_to_top(temp_layer - 1, pre_loc)
                # Here's a tricky one, because of the % operation, if temp_loc is even, temp_loc % 2 = 0!
                # and temp_loc % 2 = 1 if temp_loc is odd! so, the ind array is reversed.
                ind = [1, 0]
                if last_num == 1:
                    ind = [0, 1]
                return ind[temp_loc % 2]
            pass
        return recur_to_top(n, k)

    def kth_with_parity_check(self, n: int, k: int) -> int:
        # ?????
        pass

t = TheKthGrammarSymbol()
# print(t.kth_grammar(3, 1))
# print(t.kth_3_recursive(4, 1))
# print(t.kth_3(30, 434991989))
# print(t.kth_3(6, 26))
# print(t.kth_with_parity_check(4, 3))
