# Divide and conquer
def merge_sort(data, start, end):
    # Base-case
    if start < end:
        mid = (start + end) // 2

        # Divide the array into 2 parts
        merge_sort(data, start, mid)
        merge_sort(data, mid+1, end)
        merge(data, start, mid, end)


def merge(data, start, mid, end):
    # build temp array to avoid modifying the original contents
    temp = [0] * (end - start + 1)

    i, j, k = start, mid+1, 0

    # While both sub-array have values, then try and merge them in sorted order
    while i <= mid and j <= end:
        if data[i] <= data[j]:
            # The smaller value gets put next in the sub array temp
            temp[k] = data[i]
            i += 1
            k += 1
        else:
            temp[k] = data[j]
            j += 1
            k += 1

    # Add the rest of the values from the left sub-array into the result
    while i <= mid:
        temp[k] = data[i]
        k += 1
        i += 1

    # If the left side of the array left out of values, if the right sub-array has values left
    # Add the rest of the values from the right sub-array into the result
    while j <= end:
        temp[k] = data[j]
        k += 1
        j += 1

    for i in range(start, end+1):
        data[i] = temp[i - start]


arr = [4, 1, 3, 2, 0, -1, 7, 10, 9, 20]
merge_sort(arr, 0, len(arr)-1)
# print(arr) [-1, 0, 1, 2, 3, 4, 7, 9, 10, 20]


