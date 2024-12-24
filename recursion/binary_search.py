
def binary_search(arr, left, right, target):
    if left > target:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if target < arr[mid]:
        return binary_search(arr, left, mid-1, target)

    return binary_search(arr, mid+1, right, target)


res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 0, 10, 3)

assert res == 2, 'Wrong index returned'
