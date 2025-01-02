def generate_parentheses(num):
    ans = []

    def backtrack(op, cl, txt):
        if op == num and cl == num:
            ans.append(txt)
            return

        if op < num:
            backtrack(op + 1, cl, txt + "(")
        if cl < op:
            backtrack(op, cl + 1, txt + ")")

    backtrack(0, 0, "")
    return ans


print(generate_parentheses(3))
print(generate_parentheses(4))
