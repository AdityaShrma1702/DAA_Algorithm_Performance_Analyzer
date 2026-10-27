from algorithms import bubble_sort, merge_sort, quick_sort, linear_search, binary_search

data = [64, 25, 12, 22, 11]
print("Original array:", data)
print("Bubble Sort:", bubble_sort(data))
print("Merge Sort:", merge_sort(data))
print("Quick Sort:", quick_sort(data))

sorted_data = [11, 12, 22, 25, 64]
target = 22
print(f"\nSearching for {target} in {sorted_data}")
print("Linear Search index:", linear_search(sorted_data, target))
print("Binary Search index:", binary_search(sorted_data, target))
