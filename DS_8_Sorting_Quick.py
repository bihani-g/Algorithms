# implementing quick sort

class Quicksort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        self.quick_sort(0, len(self.nums) - 1)

    def quick_sort(self, low, high): # recursion part -- logN function calls
        # low is the index of the first item
        # high is the index of the last item
        if low >= high:
            return

        pivot_index = self.partition(low, high)

        # call partition recursively on left subarray
        self.quick_sort(low, pivot_index - 1)

        # call partition recursively on right subarray
        self.quick_sort(pivot_index + 1, high)

    def partition(self, low, high): # O(n)
        pivot_index = (low + high) // 2  # use middle item as pivot

        self.nums[pivot_index], self.nums[high] = self.nums[high], self.nums[pivot_index] # swap pivot item with last item in array

        # compare all the other items from low to high with pivot; if less than pivot value then swap item with low and increment low
        for j in range(low, high):
            if self.nums[j] <= self.nums[high]:
                self.nums[j], self.nums[low] = self.nums[low], self.nums[j]
                low += 1

        self.nums[low], self.nums[high] = self.nums[high], self.nums[low]  # swap final 'low' index item with 'high' index item (pivot item)

        # return with the index of pivot item
        return low


if __name__ == '__main__':
    x = [1, -4, 0, 10, 5, 4, 3, 100]
    algo = Quicksort(x)
    algo.sort()
    print(x)


