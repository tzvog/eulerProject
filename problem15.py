UP = 'u'
RIGHT = 'r'
counter = 0

def up_and_right(n, k):
    """
    a function to figure out my paths
    :param n: the amount right we wanna go
    :param k: the amount left we wanna go
    :return:
    """

    # testing bad cases due to talpi tests
    if n == 0 and k == 0 or k < 0 or n < 0:
        return None

    # call the up and right function
    up_and_right_helper(n, k)

    global counter

    print(counter)



def up_and_right_helper(right, up, directions=''):
    """
    a recursive function to print the directions which i can go
    :param right: the amount of right i need to go up
    :param up: the amount up i need to go
    :param directions: my directions i currently went
    :param answers:
    :return: if i made it to the end or path not accessible return
    """

    # if both locations are found no need for
    # further searching we should a have our path
    if right == 0 and up == 0:
        global counter
        counter += 1
        return

    # if we have found all our ns keep going up with k
    if right == 0 and up != 0:
        up_and_right_helper(right, up - 1, directions + UP)
        return
    # if we have found all our ks keep going with ns
    elif up == 0 and right != 0:
        up_and_right_helper(right - 1, up, directions + RIGHT)
        return

    # start path with going up
    up_and_right_helper(right, up - 1, directions + UP)

    # start path with going right
    up_and_right_helper(right - 1, up, directions + RIGHT)


if __name__ == '__main__':
    up_and_right(20,20)