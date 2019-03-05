def time_converter(time):

    old = [int(time[0:2]), time[3:5]]

    if old[0] == 0 and old[1] == '00':
        return "12:00 a.m."
    elif old[0] == 12:
        return "{}:{} p.m.".format(old[0], old[1])
    elif old[0] < 10:
        return "{}:{} a.m.".format(old[0], old[1])
    elif old[0] > 12:
        old[0] -= 12
        return "{}:{} p.m.".format(old[0], old[1])


if __name__ == '__main__':
    # print("Example:")
    # print(time_converter('12:30'))
    #
    # # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
