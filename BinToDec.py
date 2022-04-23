# binary to decimal converter
bin = input("Enter a binary number: ")
dec = 0
for i in range(len(bin)):
    dec += int(bin[i]) * 2 ** (len(bin) - i - 1)
print("Decimal number:", dec)
