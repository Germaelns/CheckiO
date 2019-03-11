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
        if '2d{}'.format(sides) not in buffer:
            matrix = np.zeros([sides, sides])

            for i in range(1, sides + 1):
                for j in range(1, sides + 1):
                    matrix[i - 1][j - 1] = i + j

            counts = dict()

            for num in range(2, sides * 2 + 1):
                counts[num] = np.count_nonzero(matrix == num) * 1 / sides ** 2
            buffer['2d{}'.format(sides)] = counts

            if '{}d{}'.format(dice_number, sides) == '2d{}'.format(sides):
                return buffer['2d{}'.format(sides)][target]

        two_dice = buffer['2d{}'.format(sides)]

        for dice in range(3, dice_number + 1):

            num_matrix = np.zeros([sides, len(two_dice)], int)
            row = -1
            maximum = 0
            for i in num_matrix:
                row += 1
                for j in range(0, len(i)):
                    num_matrix[row][j] = row + 2 + j + 1
                    if num_matrix[row][j] > maximum:
                        maximum = num_matrix[row][j]
            num_matrix = np.transpose(num_matrix)
            counts = dict()

            for i in range(dice, maximum + 1):
                counts[i] = 0

            for number in range(dice, maximum + 1):
                row = -1
                for i in num_matrix:
                    row += 1
                    for j in range(0, len(i)):
                        if number == num_matrix[row][j]:
                            counts[number] = counts[number] + 1/sides * two_dice[row + dice - 1]

            if '{}d{}'.format(dice, sides) not in buffer:
                buffer['{}d{}'.format(dice, sides)] = counts
            two_dice = counts
        return two_dice[target]


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
