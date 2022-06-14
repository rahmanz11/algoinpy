def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

arr = [5, 1, 2, 12, 13, 3, 4, 6, 7, 8, 10, 11, 9]
print(quicksort(arr))