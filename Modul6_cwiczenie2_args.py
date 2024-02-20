#Napisz funkcję, która przyjmuje listę słów i zwraca słowo, które występuje najczesciej.
#Funkcja powinna przyjmowac argumenty nazwane *args oraz ignore_case z wartością domyślną True
# który będzie oznaczał, czy ignorować wielkość liter podczas zliczania wystąpień.

from collections import Counter

def most_common_word(*args, ignore_case = True):
    words = {}
    for arg in args:
        arg = arg.lower() if ignore_case else arg
        words[arg] = words.get(arg, 0) + 1

    for word, occurences in words.items():
        if occurences == max(words.values()):
            return word

print(most_common_word('dog','cat','mouse','dog'))