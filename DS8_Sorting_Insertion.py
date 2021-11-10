# insertion sort implementation

class InsertionSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        for i in range(1, len(self.nums)):
            j = i
            while j > 0:
                if self.nums[j] < self.nums[j - 1]:
                    print("swapping elements...")
                    self.nums[j - 1], self.nums[j] = self.nums[j], self.nums[j - 1]

                j -= 1

        print(f"sorted array: {self.nums}")


# sort people based on age

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # we have to define the 'less than' function to let Python know how to interpret the < and > operators
    # when we use < then Python calls this function to decide what object is smaller and what is greater
    def __lt__(self, other):
        return self.age < other.age

    # string representation of the object (when we use the print() function then this function is called)
    def __repr__(self):
        return str(self.name)


def sort_people(people):
    for i in range(1, len(people)):
        j = i
        while j > 0:
            if people[j] < people[j - 1]:
                print("swapping elements...")
                people[j - 1], people[j] = people[j], people[j - 1]
            j -= 1

    print(f"sorted array: {people}")


if __name__ == '__main__':
    # ax = InsertionSort([-5, 5, 1, 0, -4, -1, 8, 3])
    # ax.sort()

    people = [Person('Ana', 23), Person('John', 67), Person('Ray', 45)]
    sort_people(people)
