def frequency_sort(items: list):

    result, count = list(), dict()

    for item in items:
        if item not in count:
            item_count = items.count(item)
            count[item] = item_count

    count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    for item in count:
        for num in range(0, item[1]):
            result.append(item[0])

    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4, 2]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4, 2])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
