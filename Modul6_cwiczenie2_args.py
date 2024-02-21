#Napisz funkcję, która przyjmuje listę słów i zwraca słowo, które występuje najczesciej.
#Funkcja powinna przyjmowac argumenty nazwane *args oraz ignore_case z wartością domyślną True
# który będzie oznaczał, czy ignorować wielkość liter podczas zliczania wystąpień.

# WERSJA KACPRA
# def most_common_word(*args, ignore_case = True):
#     words = {}
#     for arg in args:
#         arg = arg.lower() if ignore_case else arg #tam jest if ignore_case == True ale sie nie pisze tego
#         words[arg] = words.get(arg, 0) + 1
#
#     for word, occurences in words.items():
#         if occurences == max(words.values()):
#             return word
#
# print(most_common_word('dog','cat','mouse','Dog','CAT','Cat', ignore_case=True))

#POPRAWIONA WERSJA PRZEZ CHAT GPT
def most_common_word(*args, ignore_case=True):
    words = {}
    for arg in args:
        arg = arg.lower() if ignore_case else arg
        words[arg] = words.get(arg, 0) + 1

    max_occurrences = max(words.values())
    most_common_words = [(word, occurrences) for word, occurrences in words.items() if occurrences == max_occurrences]

    return most_common_words

result = most_common_word('dog', 'cat', 'mouse', 'Dog', 'CAT', 'Cat', ignore_case=True)
for word, occurrences in result:
    print(f"Najczęściej występujące słowo: '{word}', Ilość wystąpień: {occurrences}")

print(most_common_word('dog', 'cat', 'mouse', 'Dog', 'CAT', 'Cat', ignore_case=True))
