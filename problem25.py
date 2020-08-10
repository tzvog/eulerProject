def fibo_counter():

    a = 1
    b = 1
    counter = 0

    while True:

        counter += 1

        c = a
        a += b
        b = c

        if len(str(a)) >= 1000:
            print(counter)
            break


if __name__ == '__main__':
    fibo_counter()
