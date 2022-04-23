# Count the vowels in a string
# regex kullanarakta yapılabilir.

str = input("Enter a string: ")
vowels = 0
for i in range(len(str)):
    if str[i] in "aeiouöüıAEIOUÖÜİ":
        vowels += 1
print("Number of vowels:", vowels)