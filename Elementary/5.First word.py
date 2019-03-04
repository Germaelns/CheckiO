def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    text = text.replace(",", " ").replace(".", " ").split()
    return text[0]


if __name__ == '__main__':
    print(first_word("Hello, bitches."))
