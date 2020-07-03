'Write a binary search function.'
'It should take a sorted sequence and the item it is looking for.'
'It should return the index of the item if found.'
'It should return -1 if the item is not found.'


def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = -1
result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
