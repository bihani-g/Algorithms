# selection sort implementation

class SelectionSort:

    def __init__(self, nums):
        self.nums = nums

    def swap_min(self, i):
        min_j = i
        for j in range(i, len(self.nums)):
            if self.nums[j] < self.nums[min_j]:
                min_j = j
        print("swapping elements...")
        print(f"before swap: {self.nums}")
        self.nums[i], self.nums[min_j] = self.nums[min_j], self.nums[i]
        print(f"after swap: {self.nums}")

    def sort(self):
        i = 0
        while i < len(self.nums)-1:
            self.swap_min(i)
            i += 1

        print(f"Final sorted: {self.nums}")


if __name__ == '__main__':
    algo = SelectionSort([1, -4, 8, 5, 3, 2, -50, 26, 28, -5, 10])
    algo.sort()




