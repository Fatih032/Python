# Binary Search Algorithm
# mixed list
lst = [23,53,1,21,45,67,89,12,34,56,78,90,11,33,55,77,99,22,44,66,88,10,32,54,76,98,20,42,64,86,9,31,53,75,97,19,41,63,85,8,30,52,74,96,18,40,62,84,7,29,51,73,95,17,39,61,83,6,28,50,72,94,16,38,60,82,5,27,49,71,93,15,37,59,81,4,26,48,70,92,14,36,58,80,3,25,47,69,91,13,35,57,79,2,24,46,68,90]

def binary_search(lst, l, r, x):
    lst.sort()
    if r >= l:
        mid = l + (r - l) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return binary_search(lst, l, mid - 1, x)
        else:
            return binary_search(lst, mid + 1, r, x)
    else:
        return -1
result = binary_search(lst, 0, len(lst) - 1, 70)

if result != -1:
    print("Element is present at index", result)
    print(lst[result])
else:
    print("Element is not present in array")




# FizzBuzz
# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
''' def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i) '''