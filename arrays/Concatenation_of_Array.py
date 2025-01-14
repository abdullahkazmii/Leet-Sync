from typing import List


# approach - 1
def approach_1():
    nums = [1, 2, 3, 4, 5]
    nums.extend(nums)
    print("Approach", nums)


# approach - 2
def approach_2():
    nums = [1, 2, 3, 4, 5]
    print("Approach", nums * 2)


def approach_3():
    nums = [1, 2, 3, 4, 5]
    print("Approach", nums + nums)


approach_1()
approach_2()
approach_3()
