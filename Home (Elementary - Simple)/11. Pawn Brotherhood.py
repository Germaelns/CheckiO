import string


def safe_pawns(pawns: set) -> int:

    cols = list(string.ascii_lowercase[:9])
    cols.insert(0, "0")
    safe = set()

    if len(pawns) > 8:
        return 0

    for field in range(1, 9):
        for pawn in pawns:
            if pawn[1] == '8':
                pass
            elif pawn[1] == str(field):
                diags = ["", ""]
                diags[0] = str(cols[cols.index(pawn[0]) + 1]) + str(int(pawn[1]) + 1)
                diags[1] = str(cols[cols.index(pawn[0]) - 1]) + str(int(pawn[1]) + 1)
                for diag in diags:
                    if diag in pawns:
                        safe.add(diag)

    return len(safe)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    safe_pawns({"a8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"})
    safe_pawns({"a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"})
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
