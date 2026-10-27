def bubble_sort(values):
    arr = values.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def merge_sort(values):
    if len(values) <= 1:
        return values.copy()
    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def quick_sort(values):
    arr = values.copy()
    def sort(lo, hi):
        if lo >= hi:
            return
        pivot = arr[(lo + hi) // 2]
        i, j = lo, hi
        while i <= j:
            while arr[i] < pivot: i += 1
            while arr[j] > pivot: j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1; j -= 1
        if lo < j: sort(lo, j)
        if i < hi: sort(i, hi)
    sort(0, len(arr) - 1)
    return arr

def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search(sorted_values, target):
    low, high = 0, len(sorted_values) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_values[mid] == target:
            return mid
        if sorted_values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
