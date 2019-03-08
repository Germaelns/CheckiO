FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]


def checkio(number):
    number = int(number)
    result = ""

    if number < 10:
        result = FIRST_TEN[number - 1]
    elif 9 < number < 100:
        if number < 20:
            result = SECOND_TEN[number - 10]
        elif number > 19:
            number = str(number)
            if int(number) % 10 == 0:
                result = OTHER_TENS[int(number[0])-2]
            else:
                result = OTHER_TENS[int(number[0])-2] + " " + FIRST_TEN[int(number[1]) - 1]
    elif number > 99:
        number = str(number)
        result = FIRST_TEN[int(number[0]) - 1] + " hundred"
        number = int(number) % 100
        if 0 < number < 10:
            result += " " + FIRST_TEN[number - 1]
        elif 9 < number < 100:
            if number < 20:
                result += " " + SECOND_TEN[number - 10]
            elif number > 19:
                number = str(number)
                if int(number) % 10 == 0:
                    result += " " + OTHER_TENS[int(number[0]) - 2]
                else:
                    result += " " + OTHER_TENS[int(number[0]) - 2] + " " + FIRST_TEN[int(number[1]) - 1]

    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    checkio(100)
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio("101   ") == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
