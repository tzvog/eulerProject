def calculate_word_val(x):

    total = 0

    for i in x:
        total += ((ord(i) - ord('A')) + 1)

    return total


def read_names():

    # reads the file names and removes the parenthesis
    fd = open("p022_names.txt")
    names_list = fd.read().split(',')
    names_list.sort()
    names_list = [x[1:-1] for x in names_list]

    total_sum = 0

    for name_location in range(len(names_list)):

        name_val = calculate_word_val(names_list[name_location])
        total_sum += (name_val * (name_location + 1))

    print(total_sum)


if __name__ == '__main__':
    read_names()
