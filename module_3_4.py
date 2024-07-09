# Используем цикл for
def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words


# Используем генератор списка
def single_root_words_new(root_word, *other_words):
    return [s for s in other_words if s.lower() in root_word.lower() or root_word.lower() in s.lower()]


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))

print(single_root_words_new('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words_new('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
