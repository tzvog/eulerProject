import math

def findlargestprime():

    current = 600851475143
    sqruted = int(math.sqrt(current))
    retVal = 0

    for i in range(2, sqruted):

        if current % i == 0:
            retVal = i
            while (current % i) == 0:
                current /= i

        if current < sqruted:
            break

    # checks if whats left is bigger than the current return value
    if current > retVal:
        retVal = int(current)

    print(retVal)


if __name__ == '__main__':
    findlargestprime()