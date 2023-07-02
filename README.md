# Sorter
This is a simple Python class that implements the five most common sorting algorithms (selection sort, bubble sort, insertion sort, merge sort, quick sort) which was made as one of the assignments for Python classes and training. The sort method takes an algorithm name as input and calls the corresponding method.

Usage is simple, for example:
```
    nums = [x for x in random.sample(range(1000), 100)]
    Sorter(nums).sort("quick_sort")
    print(nums)
```

It is not meant to be used in production really, since the better way to sort list is using built-in sorted function. This class could simply be made as the following (even though it makes no sense in this case):

```
class Sorter:
    def __init__(self, data):
        self.data = data

    def sort(self):
        self.data = sorted(self.data)
```

But, you can use this for educational purposes and try to improve on it. So, give it a try.
