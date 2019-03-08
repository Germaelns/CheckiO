from typing import List


def checkio(game_result: List[str]) -> str:

    for index in range(0, 3):
        if game_result[0][index] == game_result[1][index] == game_result[2][index] and game_result[0][index] is not '.':
            return game_result[0][index]
        elif game_result[index][0] == game_result[index][1] == game_result[index][2] and game_result[index][0] is not '.':
            return game_result[index][0]

    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] is not '.':
        return game_result[0][0]
    elif game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[0][2] is not '.':
        return game_result[0][2]

    return "D"


if __name__ == '__main__':
    checkio(["X.O", "XX.", "XOO"])

    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")