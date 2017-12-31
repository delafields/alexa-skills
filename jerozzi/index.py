import logging
import os
from flask import Flask, json, render_template
from flask_ask import Ask, request, session, question, statement
from random import sample, choice
from helpers import check_numbers, map_challenge_idxs

from challenges import challenges

app = Flask(__name__)
ask = Ask(app, "/")

logger = logging.getLogger()
logging.getLogger('flask_ask').setLevel(logging.INFO)


@ask.launch
def welcome():
    return statement(render_template("welcome"))


@ask.intent("NewGameIntent")
def new_game_one():
    return question(render_template("new_game"))


@ask.intent("NumPlayersIntent", convert={'number_of_players': int})
def new_game_two(number_of_players):
    session.attributes['number_of_players'] = number_of_players

    num_challenges = map_challenge_idxs(challenges)

    session.attributes['num_challenges'] = num_challenges

    return question(render_template("get_names").format(number_of_players))


@ask.intent("GetTwoPlayerNamesIntent")
def new_game_three(player_one_name, player_two_name):

    player_list = [player_one_name, player_two_name]

    session.attributes['player_names'] = player_list

    numbers_match = check_numbers(session.attributes['player_names'],
                                  session.attributes['number_of_players'])

    if numbers_match:
        return question(
            render_template("two_player_intro").format(*player_list))
    else:
        return question(render_template("names_unequal_number"))


@ask.intent("GetThreePlayerNamesIntent")
def new_game_three(player_one_name, player_two_name, player_three_name):

    player_list = [player_one_name, player_two_name, player_three_name]

    session.attributes['player_names'] = player_list

    numbers_match = check_numbers(session.attributes['player_names'],
                                  session.attributes['number_of_players'])

    if numbers_match:
        return question(
            render_template("three_player_intro").format(*player_list))
    else:
        return question(render_template("names_unequal_number"))


@ask.intent("GetFourPlayerNamesIntent")
def new_game_three(player_one_name, player_two_name, player_three_name,
                   player_four_name):

    player_list = [
        player_one_name, player_two_name, player_three_name, player_four_name
    ]

    session.attributes['player_names'] = player_list

    numbers_match = check_numbers(session.attributes['player_names'],
                                  session.attributes['number_of_players'])

    if numbers_match:
        return question(
            render_template("four_player_intro").format(*player_list))
    else:
        return question(render_template("names_unequal_number"))


@ask.intent("GetFivePlayerNamesIntent")
def new_game_three(player_one_name, player_two_name, player_three_name,
                   player_four_name, player_five_name):

    player_list = [
        player_one_name, player_two_name, player_three_name, player_four_name,
        player_five_name
    ]

    session.attributes['player_names'] = player_list

    numbers_match = check_numbers(session.attributes['player_names'],
                                  session.attributes['number_of_players'])

    if numbers_match:
        return question(
            render_template("five_player_intro").format(*player_list))
    else:
        return question(render_template("names_unequal_number"))


@ask.intent("GetSixPlayerNamesIntent")
def new_game_three(player_one_name, player_two_name, player_three_name,
                   player_four_name, player_five_name, player_six_name):

    player_list = [
        player_one_name, player_two_name, player_three_name, player_four_name,
        player_five_name, player_six_name
    ]

    session.attributes['player_names'] = player_list

    numbers_match = check_numbers(session.attributes['player_names'],
                                  session.attributes['number_of_players'])

    if numbers_match:
        return question(
            render_template("six_player_intro").format(*player_list))
    else:
        return question(render_template("names_unequal_number"))


@ask.intent("GetSevenPlayerNamesIntent")
def new_game_three(player_one_name, player_two_name, player_three_name,
                   player_four_name, player_five_name, player_six_name,
                   player_seven_name):

    player_list = [
        player_one_name, player_two_name, player_three_name, player_four_name,
        player_five_name, player_six_name, player_seven_name
    ]

    session.attributes['player_names'] = player_list

    numbers_match = check_numbers(session.attributes['player_names'],
                                  session.attributes['number_of_players'])

    if numbers_match:
        return question(
            render_template("seven_player_intro").format(*player_list))
    else:
        return question(render_template("names_unequal_number"))


@ask.intent("GetEightPlayerNamesIntent")
def new_game_three(player_one_name, player_two_name, player_three_name,
                   player_four_name, player_five_name, player_six_name,
                   player_seven_name, player_eight_name):

    player_list = [
        player_one_name, player_two_name, player_three_name, player_four_name,
        player_five_name, player_six_name, player_seven_name, player_eight_name
    ]

    session.attributes['player_names'] = player_list

    numbers_match = check_numbers(session.attributes['player_names'],
                                  session.attributes['number_of_players'])

    if numbers_match:
        return question(
            render_template("eight_player_intro").format(*player_list))
    else:
        return question(render_template("names_unequal_number"))


@ask.intent("NextRoundIntent")
def get_challenge():

    num_challenges = session.attributes['num_challenges']
    players = session.attributes['player_names']

    random_challenge_number = choice(num_challenges)  # rand number
    random_challenge = challenges[random_challenge_number]

    num_challenges.remove(random_challenge_number)  # removes number
    session.attributes['num_challenges'] = num_challenges
    session.attributes['removed_challenge'] = random_challenge_number

    challenge_message = random_challenge['challenge_message']
    num_participants = random_challenge['names_to_add']

    if len(num_challenges) > 1:
        if num_participants == 0:
            return question(challenge_message)
        else:
            rand_players = sample(players, k=num_participants)
            return question(challenge_message.format(*rand_players))
    elif len(num_challenges) == 1:
        if num_participants == 0:
            return statement(challenge_message)
        else:
            rand_players = sample(players, k=num_participants)
            return statement(challenge_message.format(*rand_players))
    else:
        return statement(render_template("game_over"))


@ask.intent("RepeatChallengeIntent")
def repeat_challenge():

    players = session.attributes['player_names']

    challenge_number_to_repeat = session.attributes['removed_challenge']
    random_challenge = challenges[challenge_number_to_repeat]

    challenge_message = random_challenge['challenge_message']
    num_participants = random_challenge['names_to_add']

    if num_participants == 0:
        return question(challenge_message)
    else:
        rand_players = sample(players, k=num_participants)
        return question(challenge_message.format(*rand_players))


@ask.intent("EndGameIntent")
def end_game():

    return statement(render_template("end_game"))


if __name__ == '__main__':
    app.run()
