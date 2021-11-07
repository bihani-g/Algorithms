# implementing bogo sort

import random


class BogoSort:

    def __init__(self, nums):
        self.nums = nums

    def is_sorted(self):
        for i in range(len(self.nums) - 1):
            if self.nums[i] > self.nums[i + 1]:
                return False
        return True

    def shuffle(self):  # shuffling using the Fisher Yates approach
        # for i from n-1 to 0, j = random (0 to i+1), exchange i and j
        for i in range(len(self.nums) - 2, -1, -1):
            j = random.randint(0, i + 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def sort(self):
        while not self.is_sorted():
            print('Shuffling...')
            self.shuffle()  # random permutation bogo sort

        print(f"sorted array {self.nums}")













# bogo sort practice

class BogoSort_new:

    def __init__(self, nums):
        self.nums = nums

    def is_sorted(self):
        for i in range(len(self.nums)-1):
            if self.nums[i] > self.nums[i+1]:
                return False
        return True

    def shuffle(self): # shuffling using the Fisher Yates approach
        for i in range(len(self.nums)-2, -1, -1):
            j = random.randint(0, i+1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def sort(self):

        while not self.is_sorted():
            print('shuffling array...')
            self.shuffle()

        print(f"final sorted array: {self.nums}")






if __name__ == '__main__':
    algorithm = BogoSort_new([1,-4,5,8,2,3,-5,10])
    algorithm.sort()
















