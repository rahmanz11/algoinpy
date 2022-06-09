def find_smallest_value(arr):
    smallest_index = 0
    smallest_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_index = i
    return smallest_index
    
class SelSort:
    def __init__(self, array) -> None:
        self.array = array

    def selection_sort(self):
        new_arr = []
        for i in range (len (self.array)):
            smallest_index = find_smallest_value(self.array)
            new_arr.append(self.array.pop(smallest_index))

        return new_arr

        
arr = [5, 1, 2, 12, 13, 3, 4, 6, 7, 8, 10, 11, 9]
b = SelSort(arr)
print(b.selection_sort())