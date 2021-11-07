# bubble sort implementation

class BubbleSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        for i in range(len(self.nums) - 1):
            for j in range(len(self.nums) - i - 1):
                if self.nums[j] > self.nums[j + 1]:
                    print(f"swapping {self.nums[j]} and {self.nums[j + 1]}")
                    self.nums[j], self.nums[j + 1] = self.nums[j + 1], self.nums[j]

        print(f"sorted array: {self.nums}")


if __name__ == '__main__':
    algo = BubbleSort([1, -4, 5, 8, 2, 3, -5, 10])
    algo.sort()
