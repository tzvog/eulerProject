import math

def digits_sum():

    two_pow = str(int(math.pow(2, 1000)))

    sum = 0

    for i in two_pow:
        sum += int(i)

    print(sum)


if __name__ == '__main__':
    digits_sum()