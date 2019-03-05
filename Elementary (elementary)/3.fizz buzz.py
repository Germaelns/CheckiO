def checkio(numbers: list) -> list:
    result = list()
    for number in numbers:
        if number % 3 is 0 and number % 5 is 0:
            result.append("Fizz Buzz")
        elif number % 5 is 0:
            result.append("Buzz")
        elif number % 3 is 0:
            result.append("Fizz")
        else:
            result.append(number)

    return result


if __name__ == '__main__':
    checkio([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
