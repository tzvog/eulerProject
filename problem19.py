def sunday_counter():

    sundays_count = 0
    days_count = 5

    for i in range(1901, 2001):

        for j in range(1,13):

            # checks if we have reached a sunday
            if (days_count % 7) == 0:
                sundays_count += 1

            # checks how many days to add to the day counter
            if j == 2:

                if (i % 4) == 0:
                    days_count += 29
                else:
                    days_count += 28
            elif (j == 9) or (j == 4) or (j == 6) or (j == 11):
                days_count += 30
            else:
                days_count += 31

    print(sundays_count)


if __name__ == '__main__':
    sunday_counter()