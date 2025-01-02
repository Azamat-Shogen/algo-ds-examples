
def unique_paths(m, n):

    def rec(r, c, h={}):

        if r == 1 or c == 1:
            return 1

        if (r, c) in h:
            return h[(r, c)]

        h[(r, c)] = rec(r-1, c, h) + rec(r, c-1, h)
        return h[(r, c)]

    return rec(m, n)


print(unique_paths(3, 2))  # 3
print(unique_paths(3, 7))  # 28


def min_path_sum(grid):
    def rec(row, col, memo={}):
        # if we're out of bounds
        if row < 0 or col < 0:
            return float('inf')

        # if we're at the starting point
        if row == 0 and col == 0:
            return grid[row][col]

        # memoization to avoid recalculating
        if (row, col) in memo:
            return memo[(row, col)]

        # recursively calculate the minimum path sum
        memo[(row, col)] = grid[row][col] + min(rec(row - 1, col, memo), rec(row, col - 1, memo))
        return memo[(row, col)]

    # start from the bottom-right corner
    return rec(len(grid) - 1, len(grid[0]) - 1)


g = [[1,3,1],[1,5,1],[4,2,1]]
print(min_path_sum(g))
