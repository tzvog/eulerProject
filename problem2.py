def fourmilfibo():
    """

    :return:
    """

    a = 0
    b = 2
    curSum = 0

    while(a < 4000000):

        c = a
        a += b
        b = c

        if (a % 2) == 0:
            curSum += a

    print(curSum)

if __name__ == '__main__':
    fourmilfibo()
