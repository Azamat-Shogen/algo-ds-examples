def permute(nums):
    n = len(nums)
    ans, sol = [], []

    def backtrack():
        if len(sol) == n:
            ans.append(sol[:])
            return

        for item in nums:
            if item not in sol:
                sol.append(item)
                backtrack()
                sol.pop()

    backtrack()
    return ans


print(permute([1, 2, 3]))
