def flat_list(array):

    def flat_inside(array):
        for item in array:
            if type(item) is not list:
                result.append(item)
            else:
                flat_inside(item)

    result = list()
    flat_inside(array)
    return result


if __name__ == '__main__':
    # assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
