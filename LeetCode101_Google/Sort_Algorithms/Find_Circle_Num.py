class Solution:
    province = 0  # to calculate how many province

    def find_circle_num(self, isConnected: [[int]]) -> int:
        # included = [0 for i in range(len(isConnected))]  this process could add in isConnected: like [1,1][2,2] etc.
        # to calculate how many province (how many city is connected), should do the iteration in each city
        def find_circle_recursive(ind: int):
            if isConnected[ind][ind] == 0:
                return
            isConnected[ind][ind] = 0
            zeros = 0  # to count how many 0 in this, if it is len(isConnected) - ind, means end of the loop
            for city_No in range(len(isConnected) - ind):
                if isConnected[ind, city_No]:
                    find_circle_recursive(city_No)
                else:
                    zeros += 1
            if zeros == len(isConnected) - ind:
                Solution.province += 1
                return
            pass

        for i in range(len(isConnected[0])):
            find_circle_recursive(i)
            pass

    def find_circle_num_2(self, isConnected: [[int]]) -> int:
        Solution.province = 0

        def find_circle(ind: int):
            if not isConnected[ind][ind]:
                return
            isConnected[ind][ind] = 0
            # for city_no in range(1, len(isConnected) - ind):
            #     # not only [ind][ind + city_no] should be taken into consideration, also the [ind + city_no][ind]
            #     if isConnected[ind][ind + city_no] or isConnected[ind + city_no][ind]:
            #         find_circle(ind + city_no)
            for city_no in range(len(isConnected[0])):
                if isConnected[ind][city_no]:
                    find_circle(city_no)
            pass

        for i in range(len(isConnected[0])):
            if isConnected[i][i]:
                # isConnected[i][i] = 0
                find_circle(i)
                Solution.province += 1
            pass

        return Solution.province


s = Solution()
# print(s.find_circle_num_2([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(s.find_circle_num_2([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
