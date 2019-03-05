def checkio(number: int) -> str:
    if number % 3 is 0 and number % 5 is 0:
        return "Fizz Buzz"
    elif number % 5 is 0:
        return "Buzz"
    elif number % 3 is 0:
        return "Fizz"
    else:
        return "{}".format(number)


if __name__ == '__main__':
    checkio(5)
