
def reverse_string(s):
    if s == '':
        return ""
    return reverse_string(s[1:]) + s[0]


assert reverse_string('hello') == 'olleh'
assert reverse_string('world') == 'dlrow'