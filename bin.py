class BinSearch:
    def __init__(self, item, array) -> None:
        self.item = item
        self.array = array

    def binary_search(self):
        low = 0
        high = len(self.array) - 1
        step = 1
        while low <= high:
            print("step", step)
            step = step + 1
            mid = (low + high) // 2
            print("mid", mid)
            guess = self.array[mid]
            print("step %s mid %s guess %s", step, mid, guess)
            if guess > self.item:
                high = mid - 1
            elif guess < self.item:
                low = mid + 1
            elif guess == self.item:
                return mid
            else:
                return None

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b = BinSearch(9, arr)
print(b.binary_search())