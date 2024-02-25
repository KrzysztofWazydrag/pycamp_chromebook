from utils.lists import add_lists

def parse_integers(string_values:str, sep: object =',') -> list:
    output = []
    for element in string_values.split(sep):
        output.append(int(element))

    return output


if __name__ == '__main__':
    lista1 = parse_integers(
        input('Podaj wartości rozdzielone przecinkami: ')
    )
    lista2 = parse_integers(
        input('Podaj wartości rozdzielone przecinkami: ')
    )

    total = add_lists(lista1, lista2)
    print(total)
