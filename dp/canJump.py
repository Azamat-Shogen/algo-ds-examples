
def can_jump(nums):
    goal = len(nums)-1

    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= goal:
            print(f'test is: {i}+{nums[i]} >= {goal}, so goal becomes: {i}')
            goal = i

    return goal == 0


print(can_jump([2, 3, 1, 1, 4])) # should resulst to true