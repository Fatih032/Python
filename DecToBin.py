# decimal to binary converter
dec = int(input("Enter a decimal number: "))
bin = ""
while dec > 0:
    bin = str(dec % 2) + bin
    dec = dec // 2
print("Binary number:", bin)
