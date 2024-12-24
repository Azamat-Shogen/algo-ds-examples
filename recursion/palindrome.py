def is_palindrome(s):
    # Define the base-case / stopping the condition
    if len(s) == 0 or len(s) == 1:
        return True

    # Do some work to shrink the problem space
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])

    return False


print(is_palindrome('racecar'))

assert is_palindrome('ana'), 'Should return true'
assert not is_palindrome('world'), 'Should return False'
assert is_palindrome('racecar'), 'Should return True'
