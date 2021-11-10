# implementing shell sort

import random


class ShellSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        gap = len(self.nums) // 2


        # this is shell sort
        while gap > 0:
            print(f"Sorting for gap: {gap}")
            # this is insertion sort
            for i in range(gap, len(self.nums)):
                j = i
                while j >= gap:
                    if self.nums[j] < self.nums[j - gap]:
                        print("swapping elements...")
                        self.nums[j], self.nums[j - gap] = self.nums[j - gap], self.nums[j]  # swap items
                    j -= gap
            gap = gap // 2

        print(f"sorted array: {self.nums}")


if __name__ == '__main__':
    arr = [1] * 15
    actual = [random.randint(-50, 50) for x in arr]
    print(actual)
    ax = ShellSort(actual)
    ax.sort()
