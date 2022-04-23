# Middle letter
# orta harfi bulan python programı
def middle_letter(word):
    if len(word) % 2 == 0:
        return ""
    else:
        return word[len(word) // 2]

print(middle_letter("Python1"))