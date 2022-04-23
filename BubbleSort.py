# bubble sort algorithm
# boşluk bırakarak sayıları giriniz
#lst = [5, 3, 1, 2, 4]

lst = list(map(int, input("Enter the list of numbers: ").split()))

for i in range(len(lst)):
    for j in range(len(lst) - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)