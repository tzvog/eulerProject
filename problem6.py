import math


def sumsquareDiffennce():

    sums = 0
    times = 0

    for i in range(1, 101):
        sums += i
        times += int(math.pow(i, 2))

    sums = int(math.pow(sums, 2))

    print(sums - times)


if __name__ == '__main__':
    sumsquareDiffennce()
