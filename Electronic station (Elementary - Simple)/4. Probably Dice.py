import numpy as np


buffer = dict()


def probability(dice_number, sides, target):

    if target > sides*dice_number or dice_number == 0:
        return 0

    if dice_number == 1:
        return 1/sides
    elif '{}d{}'.format(dice_number, sides) in buffer:
        return buffer['{}d{}'.format(dice_number, sides)][target]
    else:
        if '{}d{}'.format(dice_number, sides) not in buffer:
            matrix = np.zeros([sides, sides])

            for i in range(1, sides + 1):
                for j in range(1, sides + 1):
                    matrix[i - 1][j - 1] = i + j

            counts = dict()

            for num in range(2, sides * 2 + 1):
                counts[num] = float(format(np.count_nonzero(matrix == num) * 1 / sides ** 2, '.4f'))
            buffer['2d{}'.format(dice_number, sides)] = counts

            if '{}d{}'.format(dice_number, sides) in buffer:
                return buffer['{}d{}'.format(dice_number, sides)][target]


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
