import itertools


def get_permutations():

    num_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    permutations_object = list(itertools.permutations(num_lst))

    permutations_object.sort()

    print(permutations_object[1000000])

if __name__ == '__main__':
    get_permutations()