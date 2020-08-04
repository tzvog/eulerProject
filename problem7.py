import math


def isPrime(x):

    for i in range(2, x):

        if (x % i) == 0:
            return False

    return True


def countPrimes():

    primeCounter = 0
    counter = 1

    while(primeCounter < 10001):
        counter += 1
        if(isPrime(counter)):
            primeCounter += 1

    print(counter)


if __name__ == '__main__':
    countPrimes()