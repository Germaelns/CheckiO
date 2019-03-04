def correct_sentence(text: str) -> str:
    if text[-1] is not ".":
        text = text + "."
    if not text[0].isupper():
        text = text[0].upper() + text[1:]
    print(text)
    return text


if __name__ == '__main__':
    correct_sentence("hi")
