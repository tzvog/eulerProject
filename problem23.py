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

def non_ambundnt():

    amubndent = set()

    for i in range(1, 28123):
        arr = []
        getDivisors(i, arr)
        arr.remove(i)
        divisors_sum = sum(arr)

        if divisors_sum > i:
            amubndent.add(i)

    total_sum = 0

    for i in range(1, 28123):

        filtered_1 = set(filter(lambda x: x < i, amubndent))
        filtered_2 = filtered_1.copy()
        flag = False

        for x in filtered_1:

            for y in filtered_2:

                if (x + y) == i:
                    flag = True
                    break

            if flag:
                break

        if flag:
            continue

        total_sum += i

    print(total_sum)


if __name__ == '__main__':
    non_ambundnt()