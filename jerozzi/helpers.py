# Checks to see if the number of players prompt matches
# the number of names given
def check_numbers(player_names, num_players):
    num_player_names = len(player_names)
    if num_player_names != num_players:
        return False
    else:
        return True


# Initializes an array of indexes for each challenge
def map_challenge_idxs(challenges):
    temp = []
    for i in range(0, len(challenges)):
        temp.append(i)
    return temp
