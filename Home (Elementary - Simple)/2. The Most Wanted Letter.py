def checkio(text: str) -> str:

    buffer = dict()
    text = text.lower()

    for letter in text:
        if letter == " ":
            continue
        try:
            buffer[letter] += 1
        except KeyError:
            buffer[letter] = 1

    count = 0
    result = str()

    for letter in buffer.items():

        if letter[0].isalpha():
            if int(letter[1]) == count:
                results = [letter[0], result]
                results = sorted(results, reverse=True)
                result = results[1]
            elif int(letter[1]) > count:
                count = int(letter[1])
                result = letter[0]
        else:
            continue

    return result


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
