"""Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun rises
in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith,
which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. If the
input will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the
sun!".

Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places.
"""


def sun_angle(time):

    deg_hour = 180/12
    deg_minute = deg_hour/60

    not_see = list()
    for item in range(1, 6):
        not_see.append("0"+str(item))
    for item in range(19, 24):
        not_see.append(str(item))

    if time[:2] in not_see or (time[:2] == "18" and int(time[-2:]) > 0):
        return "I don't see the sun!"
    else:
        return ((int(time[:2])-6)*deg_hour)+(float(time[-2:])*deg_minute)


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
