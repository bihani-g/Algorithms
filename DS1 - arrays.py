# #  arrays
#
# array = [10, 3, 7, 5]  # random indexing, starting with 0
#
# print(array)
#
# print(array[0])
#
# #  finding max/min in the array (linear search) --> O(N)
#
# maximum = array[0]
#
# for num in array:
#     if num > maximum:
#         maximum = num
#
# print(maximum)
#

# Interview questions

# Reversing array in place

def reverse_array(a):  # O(N) where N is length of string/array
    start = 0
    end = len(a) - 1

    while start < end:
        a[start], a[end] = a[end], a[start]
        start = start + 1
        end = end - 1

    return a


arr = [1, 2, 3, 4, 5, 6]
print(reverse_array(arr))


# Palindrome check (using slicing string)

def is_palindrome(a):
    if a == a[::-1]:  # slicing string from last position and goes backward
        return True
    return False


string = 'madam'
is_palindrome(string)


# Palindrome check (without slicing, using reverse array function)

def reverse_array(a):  # O(N) where N is length of string/array
    start = 0
    end = len(a) - 1

    while start < end:
        a[start], a[end] = a[end], a[start]
        start = start + 1
        end = end - 1

    return a


def is_palindrome(b):  # O(N) where N is length of string/array (because reversing takes O(N) time
    arr0 = list(b)
    arr1 = list(b)
    rev = reverse_array(arr1)
    print(arr0)
    print(rev)
    if arr0 == rev:  # is this array same as reverse of array
        return True
    return False


string = 'madam'
print(is_palindrome(string))


# Integer reversion (transform into list and reversing list)

def integer_reversion(num):
    num = list(str(num))
    return int(''.join(reverse_array(num)))


number = 4536
print(integer_reversion(number))


# Integer reversion (without transforming into list)

def integer_reversion(num):  # O(1) time
    rev = 0
    rem = 0

    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = int(num / 10)
    return rev


number = 4538430

if __name__ == "main":
    print(integer_reversion(number))


# Anagram problem = Total time complexity O(NlogN)+O(N) --> O(NlogN)

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    # sort the letters of the string and compare the letters with same indices

    str1 = sorted(str1)  # bottleneck because sorting has O(NlogN) time complexity
    str2 = sorted(str2)

    # check letters with the same indices

    for i in range(len(str1)):  # O(N)
        if str1[i] != str2[i]:
            return False

    return True


print(is_anagram('restfully', 'fluster'))


# Find duplicates in array (O(N) time but cannot handle -ve values and values > length of array

def find_dup(a):
    for i in a:
        if a[abs(i)] >= 0:
            a[abs(i)] = -a[abs(i)]
        else:
            print('Duplicate found: %s' % str(abs(i)))


if __name__ == '__main__':
    array = [1, 2, 3, 4, 4]
    find_dup(array)
