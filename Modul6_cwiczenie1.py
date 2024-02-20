#napisz funkcje ktora zwraca sume ale tylko liczb wyzszych niz ustalony limit.
def adding_numbers(*args, limit:int=9) ->int:

    given = []

    for num in args:
        if num > limit:
            given.append(num)

    return sum(given)

print(adding_numbers(5,6,10,15, limit=10))