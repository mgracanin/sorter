class Sorter:

    def __init__(self, data):
        self.data = data

    def selection_sort(self):
        for i in range(len(self.data)):
            min_index = i
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            if min_index != i: ## avoid swapping with itself if the minimum index is already in its place
                self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

    def bubble_sort(self):
        for i in range(len(self.data) - 1):
            is_sorted = True
            for j in range(len(self.data) - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    is_sorted = False
            if is_sorted: ## break if no swaps were made, e.g., the list is already sorted
                break

    def insertion_sort(self):
        for i in range(1, len(self.data)):
            j = i - 1
            key = self.data[i]
            while j >= 0 and self.data[j] > key:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key

    def merge_sort(self):
        if len(self.data) <= 1:
            return
        mid = len(self.data) // 2
        left = self.data[:mid]
        right = self.data[mid:]
        self.merge_sort(left)
        self.merge_sort(right)
        self.merge(left, right)

    def merge(self, left, right):
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                self.data[k] = left[i]
                i += 1
            else:
                self.data[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            self.data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            self.data[k] = right[j]
            j += 1
            k += 1

    def quick_sort(self, low, high):
        if low < high:
            pivot = self.data[high]
            i = low - 1
            for j in range(low, high):
                if self.data[j] <= pivot:
                    i += 1
                    self.data[i], self.data[j] = self.data[j], self.data[i]
            self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
            self.quick_sort(low, i)
            self.quick_sort(i + 2, high)

    def sort(self, algorithm):
        if algorithm == "selection_sort":
            self.selection_sort()
        elif algorithm == "bubble_sort":
            self.bubble_sort()
        elif algorithm == "insertion_sort":
            self.insertion_sort()
        elif algorithm == "merge_sort":
            self.merge_sort()
        elif algorithm == "quick_sort":
            self.quick_sort(0, len(self.data) - 1)


if __name__ == "__main__":
    import random

    brojevi = [x for x in random.sample(range(1000), 100)]
    sorter = Sorter(brojevi).sort("quick_sort")
    print(brojevi)