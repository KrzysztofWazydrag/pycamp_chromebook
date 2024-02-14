def pin_check(pin:str) ->bool:
    if not len(pin) == 4:
        return False

    for char in pin:
        if not char.isdigit():
            return False

    return True

print(pin_check('5533'))
print(pin_check('5433'))
print(pin_check('55343'))
print(pin_check('553'))