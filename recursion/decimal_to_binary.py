def find_binary(decimal, result):
    if decimal == 0:
        return result

    result = str(decimal % 2) + result  # Add reminder, either 1 or 0
    return find_binary(decimal // 2, result)  # Reduce the decimal value


print(find_binary(233, ''))
assert find_binary(233, '') == '11101001', "The result should equal to '11101001'."
