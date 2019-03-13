def checkio(expression):
    if expression.isupper() or expression.islower():
        return False

    brackets = list()
    for symbol in expression:
        if symbol in "(){}[]":
            brackets.append(symbol)
    counter = 0
    for i in range(0, len(brackets)):
        if brackets[i] in "{[(":
            counter += 1
            if counter > len(brackets) / 2:
                return False
        elif brackets[i] in "]})":
            if brackets[i] == ']' and brackets[i-1] == '[':
                brackets.remove(brackets[i])
                brackets.remove(brackets[i-1])
            elif brackets[i] == ')' and brackets[i-1] == '(':
                brackets.remove(brackets[i])
                brackets.remove(brackets[i-1])
            elif brackets[i] == '}' and brackets[i-1] == '{':
                brackets.remove(brackets[i])
                brackets.remove(brackets[i-1])

    if len(brackets):
        return False
    else:
        return True


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
