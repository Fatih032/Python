# Just the numbers
# sadece sayıları döndüren python kodu
def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Lütfen sayı giriniz.")

print(get_number("Sayıyı giriniz: "))