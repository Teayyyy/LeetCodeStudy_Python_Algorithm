class Solution:
    def the_solution(self, s: str, budget: int) -> int:
        '''
        Description:
            You are given a task to fix potholes in a road. The road is described bt a string "S" consisting of charact-
        ers.Each character represents a single fragment of the road. Character '.' denotes a smooth surface and 'x' den-
        otes a pothole. For example: S = "...XXX..X" means that the road start with three smooth fragments, followed by
        three potholes, followed by two smooth fragments and ending with one pothole.

        You can choose any number of consecutive potholes and fix all of them. Fxing a segment consisting of K consecut-
        ive potholes costs K + 1. In the example above, fixing the first two consecutive potholes costs 2 + 1 = 3 and
        fixing the last pothole costs 1 + 1 = 2. After these fixed, the road would look like this: ".....X..."

        You are given a budget B. You can fix multiple segments containing potholes as long as you fit in the budget.
        What is the maximum number of potholes you can fix?

        Other Examples: See picture in Wechat.

        :param s: The string denotes the entire road.
        :param budget: The total budget for repairing the potholes.
        :return: How many potholes you fix under the budget of B and the number should be the maximum.
        '''
        n = len(s)  # get the length of the road
        # special circumstances
        if n == 1 and n is ".":
            return 0
        if budget is 0:
            return 0
        pothole_fixed = 0  # recording how many potholes have been fixed
        pothole_remain = s.count('x')
        car = [0, 2]  # car starts with the beginning of the road 0 ends in 2 which because car length in 3
        has = [True, True, True]  # describe if there's 1/2/3 consecutive potholes
        last_index = 0

        while budget > 1 and pothole_remain > 0:  # When budget is 0 or 1, no holes could be fixed
            if budget >= 4:
                # TODO: try to find 3-consecutive potholes, if not, find 2 or even 1
                pass
            elif budget == 3:
                # TODO: try to find 2-consecutive potholes, if not, find 1
                pass
            elif budget == 2:
                # TODO: try to find 2-consecutive potholes
                pass

        return pothole_fixed

    def potholes_fix(self, s: str, budget: int) -> int:
        n = len(s)
        # Some special circumstances
        if n is 1 and s is '.':
            return 0
        if budget is 0:
            return 0
        pothole_fixed = 0  # Count how many fixed-holes
        pothole_remain = s.count('x')  # How many holes in total
        print("Holes: ", pothole_remain, end="\t")
        print("Budget: ", budget)
        print("The road: ", s, end="\t\n")
        pothole_position = self.find_potholes(s)
        print("Consecutive potholes and where it begins: \n\t", pothole_position)

        # Begin to fix potholes
        while budget > 0 and pothole_position:
            temp_pothole = pothole_position.pop(0)  # Get the first one in queue temp_pothole[0] is number of holes
            # if this bunch of hole could be perfectly fixed
            if temp_pothole[0] + 1 <= budget:
                pothole_fixed += temp_pothole[0]
                budget -= (temp_pothole[0] + 1)
            else:  # if temp_pothole[0] > budget, find budget - 1 holes
                pothole_fixed += (budget - 1)
                budget = 0

        return pothole_fixed  # Return the answer



    # Find the consecutive potholes (data pre-process)
    def find_potholes(self, s1: str) -> [[int]]:
        former, latter = 0, 1
        count_temp = 0
        saving_list = []
        while former <= len(s1) - 1:
            if s1[former] == 'x':
                count_temp += 1
                while latter < len(s1) - 1 and s1[latter] == 'x':  # Don't let latter out of range
                    count_temp += 1
                    latter += 1
                saving_list.append([count_temp, former])  # how many potholes and where it begins
                former = latter
                latter = former + 1
                count_temp = 0
            else:  # s1[former] == '.'
                former += 1
                latter = former + 1
        # print("Fresh: ", saving_list)
        saving_list.sort(key=lambda x: -x[0])
        # print("Sorted: ", saving_list)
        return saving_list


sss = Solution()
testString = "xx.xx.xx.xxx.x.xxxx.x"
# sss.find_potholes(testString)
# print("The total potholes fixed is :", sss.potholes_fix(testString, 17))
print("-" * 40)
print("The total potholes fixed is: ", sss.potholes_fix("...xxx...x...xxx.", 7))
print("-" * 40)
print("The total potholes fixed is: ", sss.potholes_fix("...xxxxx", 4))
print("-" * 40)
print("The total potholes fixed is: ", sss.potholes_fix("x.x.xxx....x", 14))
print("-" * 40)
print("The total potholes fixed is: ", sss.potholes_fix(".", 5))

