#napisz funkcje ktora zwraca sume ale tylko liczb wyzszych niz ustalony limit.
def adding_numbers(*args, limit = 9):

    given = []

    for num in args:
        if num > limit:
            given.append(num)

    return sum(given)

print(adding_numbers(1,5,10,15,20,2,5,6,9,99))