# Create a calculator function
def calculate(num1, num2, operator):
    if operator == 'topla':
        return num1 + num2
    elif operator == 'cıkar':
        return num1 - num2
    elif operator == 'carp':
        return num1 * num2
    elif operator == 'bol':
        return num1 / num2
    else:
        return 'Geçersiz işlem'

num1 = int(input("1. sayıyı giriniz: "))
num2 = int(input("2. sayıyı giriniz: "))
operator = input("İşlemi giriniz: ")
print(calculate(num1, num2, operator))