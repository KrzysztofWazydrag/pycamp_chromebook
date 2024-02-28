#Przygotuj funkcję, która zliczy ilość znaków w tekście zawierających się wewnątrz nawiasów okrągłych.
#NAwiasy mogą występować w tekście wielokrotnie, nigdy nie będą się w sobie zawierać.


def count_chars_between(text:str, char_start:str='(', char_end:str=(')')):
    should_i_count_char = False
    counter = 0

    for char in text:
        if char == char_end:
            should_i_count_char = False

        if should_i_count_char:
            counter += 1

        if char == char_start:
            should_i_count_char = True

    return counter

print(count_chars_between('Ala ma (kota)'))





# count_letters('(ala) ma (kota)')
# # zwróci 3 + 4
#
# count_letters('<> kod <103>', '<', '>')
# #zwróci 3
#
# count_letters('abrakadabra')
# #zwróci 0