def say_hi(name: str, age: int) -> str:
    return "Hi. My name is {} and I'm {} years old".format(name, age)


if __name__ == '__main__':
    say_hi("Nick", 25)
