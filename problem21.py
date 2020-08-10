import math

def getDivisors(n, lst):

    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):

        if (n % i == 0):

            # If divisors are equal, print only one
            if (n / i == i):
                lst.append(i)
            else:
                # Otherwise print both
                lst.append(i)
                lst.append(int(n /i))
        i = i + 1


def create_amicable():

    # ambient_dict = {}
    num_to_divisor = {}

    for i in range(1, 10000):

        arr = []
        getDivisors(i, arr)
        arr.remove(i)
        divisors_sum = sum(arr)

        num_to_divisor[i] = divisors_sum

        # if divisors_sum in ambient_dict:
        #     ambient_dict[divisors_sum].append(i)
        # else:
        #     ambient_dict[divisors_sum] = [i]

    total_sum = 0

    # goes through all the numbers
    for i in range(1, 10000):

        # checks if our number is in the dictionary
        if i in num_to_divisor:

            # gets the val in the dictionary
            val = num_to_divisor[i]

            # checks that it is not the next number
            if val == i:
                continue

            # checks that the number is in the divisor
            if val in num_to_divisor:

                # the numbers are equal
                if num_to_divisor[val] == i:
                    total_sum += (i + val)

                    # removes from the divisors dict
                    del num_to_divisor[val]
                    del num_to_divisor[i]

    print(total_sum)


if __name__ == '__main__':
    create_amicable()
