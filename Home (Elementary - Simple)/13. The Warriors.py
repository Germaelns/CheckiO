class Warrior:
    def __init__(self):
        self.health = 50
        self.damage = 5

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.damage = 7


def fight(unit_1, unit_2):

    r = 2
    while unit_1.is_alive() and unit_2.is_alive():
        if r % 2 == 0:
            unit_2.health -= unit_1.damage
            r += 1
        else:
            unit_1.health -= unit_2.damage
            r += 1

    if unit_1.is_alive():
        return True
    else:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive() == True
    assert bruce.is_alive() == False
    assert carl.is_alive() == True
    assert dave.is_alive() == False
    assert fight(carl, mark) == False
    assert carl.is_alive() == False

    print("Coding complete? Let's try tests!")
