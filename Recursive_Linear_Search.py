def recursive_linear_search(arr, key, index=0):

    if index >= len(arr):
        return -1

    if arr[index] == key:
        return index

    return recursive_linear_search(arr, key, index + 1)


nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]
key = 77
result = recursive_linear_search(nums, key)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")