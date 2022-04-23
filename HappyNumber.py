# happy number
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 2
    temp //= 10
if num == sum:
    print(num, "is a happy number")
else:
    print(num, "is not a happy number")

