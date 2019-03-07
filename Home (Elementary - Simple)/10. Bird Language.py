VOWELS = "aeiouy"


def translate(phrase):

    for letter in VOWELS:
        if letter*3 in phrase:
            phrase = phrase.replace(letter*3, letter)

    for letter in phrase:
        if letter not in VOWELS and letter is not " ":
            for vowel in VOWELS:
                phrase = phrase.replace(letter + vowel, letter + "0")

    if "0" in phrase:
        phrase = phrase.replace("0", "")

    return phrase


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
