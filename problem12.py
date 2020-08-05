def count_divisors(x):

    counter = 0

    for i in range(1, x+1):

        if(x % i) == 0:
            counter += 1

    return counter


def triangle_numbers():

    arr = [1]
    divers = [1]
    i = 2
    flag = True

    while flag:

        cur_val = arr[i - 2] + i

        arr.append(cur_val)

        if count_divisors(cur_val) > 500:
            print(cur_val)
            flag = False

        i += 1


if __name__ == '__main__':
    triangle_numbers()