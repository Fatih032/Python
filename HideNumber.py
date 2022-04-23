# Hide the credit card number
num = input("Enter a credit card number: ")
#print("Hidden credit card number:", "*" * (len(num) - 4) + num[-4:])
print(num[:4], end="")
for i in range(3,len(num)-4):
    print("*", end="")
print(num[-4:])