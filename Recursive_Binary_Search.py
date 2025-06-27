def recursive_binary_search(arr, key, start=0, end=None):

    if end is None:
        end = len(arr) - 1

    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == key:
        return mid

    elif key < arr[mid]:
        return recursive_binary_search(arr, key, start, mid - 1)
    else:
        return recursive_binary_search(arr, key, mid + 1, end)

nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]
key = 77
result = recursive_binary_search(nums, key)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")