def house(plan):

    plan = plan.strip('\n').splitlines()

    def count() -> int:
        value = 0
        remove = list()

        for string in plan:
            if "#" in string:
                value += 1
            elif "#" not in string and (string == plan[0] or string == plan[-1]):
                remove.append(plan.index(string))
            else:
                value += 1

        for index in sorted(remove, reverse=True):
            plan.remove(plan[index])

        return value

    height = count()

    plan = list(zip(*plan))

    weight = count()

    return height * weight


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
