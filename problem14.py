def max_chain():

    game_dict = {1: 1}

    for i in range(1, 1000000):

        changing = i

        length_counter = 0

        while changing not in game_dict:

            length_counter += 1

            if changing % 2 == 0:
                changing = int(changing / 2)
            else:
                changing = (changing * 3) + 1

        game_dict[i] = (length_counter + game_dict[changing])

    print(max(game_dict, key=game_dict.get))
    print(max(game_dict.values()))

if __name__ == '__main__':
    max_chain()