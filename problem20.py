import math

def factorial_digit_sum():

    hundred_factorial = str(math.factorial(100))

    total_sum = 0

    for i in hundred_factorial:
        total_sum += int(i)

    print(total_sum)


if __name__ == '__main__':
    factorial_digit_sum()