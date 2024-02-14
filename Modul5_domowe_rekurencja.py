# sum_it(5) 5+4+3+2+1 - rekurencja a nie if

def sum_it(number:int) -> int:
    if number == 0:
        return 0

    return number + sum_it(number -1)

print(sum_it(10))