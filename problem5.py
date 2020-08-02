def smallestPositivenumber():

    total = 1

    for i in range(1, 20):
        total *= i

    for j in range(1, total):

        flag = True

        for k in range(1, 20):

            if (j % k) != 0:
                flag = False
                break

        if flag:
            print(j)
            break


if __name__ == '__main__':
    smallestPositivenumber()