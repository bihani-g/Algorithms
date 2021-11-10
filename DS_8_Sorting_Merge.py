# implementing merge sort

def merge_sort(nums):

    # define the base case - keep splitting the arrays until the subarrays have just one time (or do insertion sort to have sorted subarrays)
    if len(nums) == 1:  # call merge sort recursively until no. of items per subarray =1
        return

    # divide phase
    middle_index = len(nums)//2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

    merge_sort(left_half) # call merge sort recursively on left and right half
    merge_sort(right_half)

    # conquer phase
    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j += 1

        k += 1

    # after that there may be additional items in either left or right subarray
    while i < len(left_half):
        nums[k] = left_half[i]
        k += 1
        i += 1

    while j < len(right_half):
        nums[k] = right_half[j]
        k += 1
        j += 1



if __name__ == '__main__':
    x = [1, -4, 0, 10, 5, 4, 3, 100]
    merge_sort(x)

    print(x)