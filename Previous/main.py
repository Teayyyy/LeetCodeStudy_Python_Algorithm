# 计算是否存在多个重复

def cal_duplicates(numbers):
    simple_list = []
    for item in numbers:
        if search_previous(simple_list, item):
            return True
        else:
            simple_list.append(item)
    return False
    pass


def search_previous(simple_list, item):
    if not simple_list:
        return False
    for i in simple_list:
        if i == item:
            return True
    else:
        return False


# main
numbers = input("Please Input a list of number")
numbers = numbers.split(" ")
if cal_duplicates(numbers):
    print("Find duplicates")
else:
    print("No duplicates")
