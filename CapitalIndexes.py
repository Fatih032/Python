# Büyük harflerin indeksini döndüren python kodu
def capital_indexes(word):
    indexes = []
    for i in range(len(word)):
        if word[i].isupper():
            indexes.append(i)
    return indexes
print(capital_indexes("PythoN"))