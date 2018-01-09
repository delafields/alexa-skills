import logging
import os
from flask import Flask, json, render_template
from flask_ask import Ask, request, session, question, statement, audio, current_stream

from artist_data import adlibs, artists_names_list
from helpers import get_random_adlib, get_specific_artist, format_artist_synonyms

app = Flask(__name__)
ask = Ask(app, "/")

logger = logging.getLogger()
logging.getLogger('flask_ask').setLevel(logging.INFO)


@ask.launch
def new_game():
    welcome_msg = "Welcome to rap adlibs. You can either say, give me an artist's adlib, or give me a random adlib, and guess who's it is."
    return statement(welcome_msg)


@ask.intent('RandomAdlibIntent')
def next_round():
    artist_name, artist_adlib = get_random_adlib(artists_names_list, adlibs)

    # Plays adlib–asks "guess who"
    adlib_quiz_msg = '<speak>Guess who this is <break time="500ms" /><audio src="{}" /></speak>'.format(
        artist_adlib)

    # persists the random artist's name to compare against
    # the user's guess in 'RandomAdlibAnswerIntent'
    session.attributes['adlib-artist'] = artist_name

    return question(adlib_quiz_msg)


@ask.intent('RandomAdlibAnswerIntent', mapping={'artist': 'Artist'})
def answer(artist):

    # Checks if answer is correct or a synonym for correct answer
    artist = artist.title()
    found, artist = format_artist_synonyms(artist)
    artist = artist.title()

    # The persisted random_artist from 'RandomAdlibIntent'
    winning_answer = session.attributes['adlib-artist']

    # If they got it right, say yes. If not, tell em who it is.
    if found == True and winning_answer == artist:
        msg = "You got it"
    else:
        msg = '<speak><audio src="https://s3.amazonaws.com/rap-adlibs/WRONGANSWER.mp3" /> <break time="500ms" /> it was {}</speak>'.format(
            winning_answer)

    return statement(msg)


@ask.intent('GetSpecificArtistAdlibIntent', mapping={'artist': 'Artist'})
def next_round(artist):

    # Takes the artist the user asks for,
    # returns whether we have them or not (found)
    artist = artist.title()
    response = get_specific_artist(artist, artists_names_list, adlibs)
    found = response[0]

    if found == True:
        adlib_artist = response[1]
        adlib_audio_url = response[2]
        msg = '<speak>Here is a {} adlib <break time="500ms" /><audio src="{}" /> <break time="500ms" /></speak>'.format(
            adlib_artist, adlib_audio_url)
    elif found == False:
        msg = "<speak>I don't have that artist, sorry.</speak>"

    return statement(msg)


@ask.intent('DoYouHaveIntent', mapping={'artist': 'Artist'})
def next_round(artist):

    # Takes the artist the user asks for,
    # returns whether we have them or not (found)
    response = get_specific_artist(artist, artists_names_list, adlibs)
    found = response[0]

    if found == True:
        adlib_artist = response[1]
        adlib_audio_url = response[2]
        msg = "<speak>Yeah, I have adlibs for {}, here's one <break time='500ms' /><audio src='{}' /> <break time='500ms' /></speak>".format(
            adlib_artist, adlib_audio_url)
    elif found == False:
        msg = "<speak>I don't have that artist, sorry.</speak>"

    return statement(msg)


@ask.intent('WhoDoYouHaveIntent')
def next_round():
    artists_names_sentence = ", ".join(artists_names_list)
    msg = '<speak>I have adlibs for {}</speak>'.format(artists_names_sentence)
    return statement(msg)


@ask.intent("AMAZON.PauseIntent")
def pause():
    return audio('Paused the stream').stop()


@ask.intent('AMAZON.ResumeIntent')
def resume():
    return audio('Resuming.').resume()


@ask.intent('AMAZON.StopIntent')
def stop():
    return audio('stopping').clear_queue(stop=True)


# optional callbacks
@ask.on_playback_started()
def started(offset, token):
    _infodump('STARTED Audio Stream at {} ms'.format(offset))
    _infodump('Stream holds the token {}'.format(token))
    _infodump('STARTED Audio stream from {}'.format(current_stream.url))


@ask.on_playback_stopped()
def stopped(offset, token):
    _infodump('STOPPED Audio Stream at {} ms'.format(offset))
    _infodump('Stream holds the token {}'.format(token))
    _infodump('Stream stopped playing from {}'.format(current_stream.url))


@ask.on_playback_nearly_finished()
def nearly_finished():
    _infodump('Stream nearly finished from {}'.format(current_stream.url))


@ask.on_playback_finished()
def stream_finished(token):
    _infodump('Playback has finished for stream with token {}'.format(token))


@ask.session_ended
def session_ended():
    return "{}", 200


def _infodump(obj, indent=2):
    msg = json.dumps(obj, indent=indent)
    logger.info(msg)


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
