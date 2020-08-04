import math

def pithagores():

    flag1 = False

    for i in range(1,1000):
        for j in range(1,1000):
            for k in range(1,1000):
                if (math.pow(i, 2) + math.pow(j, 2) - math.pow(k, 2)) == 0 and \
                        (i + j + k) == 1000:
                    print(i, j, k)
                    flag1 = True

            if flag1:
                break

        if flag1:
            break


if __name__ == '__main__':
    pithagores()