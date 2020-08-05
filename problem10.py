def isPrime(x):

    for i in range(2, x):

        if (x % i) == 0:
            return False

    return True


def count_primes():

    primes_sum = 0

    for i in range(2, 2000000):
        if isPrime(i):
            primes_sum += i

    print(primes_sum)


if __name__ == '__main__':
    count_primes()