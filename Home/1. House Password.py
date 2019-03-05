def checkio(data: str) -> bool:

    if len(data) < 10:
        return False

    digit, upper, lower = False, False, False

    for item in data:
        if item.isdigit():
            digit = True
        if item.islower():
            lower = True
        if item.isupper():
            upper = True
        if digit and lower and upper:
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
