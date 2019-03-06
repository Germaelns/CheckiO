import copy


def house(plan):

    plan = plan.splitlines()

    def rotate(matrix) -> list:
        rotate_matrix = copy.deepcopy(matrix)

        return rotate_matrix

    def count() -> int:
        value = 0
        remove = list()
        for index in range(0, len(plan)):
            if "#" in plan[index]:
                value += 1
            else:
                remove.append(index)

        remove = sorted(remove, reverse=True)
        for index in remove:
            plan.remove(plan[index])

        return value

    height = count()

    plan = rotate(plan)

    weight = count()

    return height*weight


if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

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
