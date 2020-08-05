def count_words():

    number_dict = {1: 3,
                   2: 3,
                   3: 5,
                   4: 4,
                   5: 4,
                   6: 3,
                   7: 5,
                   8: 5,
                   9: 4,
                   10: 3,
                   11: 6,
                   12: 6,
                   13: 8,
                   14: 8,
                   15: 7,
                   16: 7,
                   17: 9,
                   18: 8,
                   19: 8,
                   20: 6,
                   30: 6,
                   40: 5,
                   50: 5,
                   60: 5,
                   70: 7,
                   80: 6,
                   90: 6,
                   "hundred": 7,
                   "and": 3}

    total_counter = 0

    for i in range(1, 1001):

        word_coutner = 0

        cur_val = i

        if cur_val > 99:

            # get the hundred value
            cur_val_hundred = int (cur_val / 100)

            # counts up the hundred part
            word_coutner += (number_dict[cur_val_hundred] +
                             number_dict["hundred"])

            # checks that not empty
            if (cur_val_hundred * 100) != cur_val:
                word_coutner += number_dict["and"]


            cur_val -= (cur_val_hundred * 100)


        if cur_val > 19:

            # gets the tens values
            cur_val_ten = int(cur_val / 10)
            word_coutner += (number_dict[(cur_val_ten * 10)])
            cur_val -= (cur_val_ten * 10)

        if cur_val > 0:

            word_coutner += number_dict[cur_val]

        total_counter += word_coutner

    print(total_counter)


if __name__ == '__main__':
    count_words()