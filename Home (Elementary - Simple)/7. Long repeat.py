def long_repeat(line: str):

    if len(line) is not 0:
        count, before, result = 0, "", 0
        for item in line:

            if item == before:
                count += 1
            else:
                before = item
                count = 1

            if count > result:
                result = count

        return result

    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
