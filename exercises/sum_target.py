# recursive

def can_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for num in numbers:
        remainder = target - num
        if can_sum(remainder, numbers, memo) is True:
            memo[target] = True
            return True

    memo[target] = False
    return False


def how_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    for item in numbers:
        remainder = target - item
        result = how_sum(remainder, numbers, memo)
        if result is not None:
            memo[target] = result[:] + [item]
            return memo[target]

    memo[target] = None
    return None


def best_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None
    for num in numbers:
        rem = target - num
        remainder_combination = best_sum(rem, numbers, memo)
        if remainder_combination is not None:
            combination = remainder_combination + [num]

            # Update shortest_combination only if it's the shortest found
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[target] = shortest_combination
    return shortest_combination


def combination_sum(target, numbers):
    res = []

    def dfs(t, path, start):
        if t == 0:
            res.append(path)
            return

        if t < 0:
            return

        for i in range(start, len(numbers)):
            dfs(t - numbers[i], path + [numbers[i]], i)

    dfs(target, [], 0)
    return res


print(combination_sum(7, [2, 3]))
print(combination_sum(7, [5, 3, 4, 7]))
print(combination_sum(7, [2, 4]))
print(combination_sum(8, [5, 3, 2]))
print(combination_sum(8, [2, 3, 5])) 


# print(best_sum(7, [2, 3]))  # [3, 2, 2]
# print(best_sum(7, [5, 3, 4, 7]))  # [4, 3]
# print(best_sum(7, [2, 4]))  # None
# print(best_sum(8, [5, 3, 2]))  # [3, 5]
# print(best_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
# print(best_sum(300, [7, 14]))  # None

# print(how_sum(7, [2, 3]))  # [3, 2, 2]
# print(how_sum(7, [5, 3, 4, 7]))  # [4, 3]
# print(how_sum(7, [2, 4]))  # None
# print(how_sum(8, [5, 3, 2]))  # [3, 5]
# print(how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
# print(how_sum(300, [7, 14]))  # None

# time: O(n*m^2)
# space: 0(m)  m for memo


# print(can_sum(7, [2, 3]))  # True
# print(can_sum(7, [5, 3, 4, 7]))  # True
# print(can_sum(7, [2, 4]))  # False
# print(can_sum(8, [2, 3, 5]))  # True
# print(can_sum(300, [7, 14]))  # False
