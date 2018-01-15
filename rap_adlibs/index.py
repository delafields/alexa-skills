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
    card_text = "Welcome to rap adlibs! You can either say: Who do you have? Or do you have a certain artist? Or play a certain artist. Or give me a random adlib and then guess who it is."
    welcome_msg = '<speak>Welcome to rap adlibs! <break time="200ms" /> You can either say who do you have? <break time="500ms" /> Or do you have a certain artist? <break time="500ms" /> Or play a certain artist. <break time="500ms" /> Or give me a random adlib and then guess who it is.</speak>'
    return question(welcome_msg).standard_card(
        title="Welcome To Rap Adlibs",
        text=card_text,
        small_image_url='https://s3.amazonaws.com/rap-adlibs/icon_large.png',
        large_image_url='https://s3.amazonaws.com/rap-adlibs/icon_small.png'
    ).reprompt(welcome_msg)


@ask.intent('GetSpecificArtistAdlibIntent', mapping={'artist': 'Artist'})
def next_round(artist):

    if artist is None or len(artist) <= 0:
        msg = 'Your request did not include an artist'
        card_text = 'Your request did not include an artist'
    else:
        # Takes the artist the user asks for,
        # returns whether we have them or not (found)
        artist = artist.title()
        response = get_specific_artist(artist, artists_names_list, adlibs)
        found = response[0]

        if found == True:
            adlib_artist = response[1]
            adlib_audio_url = response[2]
            card_text = "Here is an adlib for {}".format(adlib_artist)
            msg = '<speak>Here is a {} adlib <break time="500ms" /><audio src="{}" /> <break time="500ms" /></speak>'.format(
                adlib_artist, adlib_audio_url)
        elif found == False:
            card_text = "I don't have that artist, sorry."
            msg = "<speak>I don't have that artist, sorry.</speak>"

    return statement(msg).simple_card(
        title="Specific Artist Adlib", content=card_text)


@ask.intent('RandomAdlibIntent')
def next_round():
    artist_name, artist_adlib = get_random_adlib(artists_names_list, adlibs)

    # Plays adlib–asks "guess who"
    adlib_quiz_msg = '<speak>Guess who this is <break time="500ms" /><audio src="{}" /></speak>'.format(
        artist_adlib)

    # persists the random artist's name to compare against
    # the user's guess in 'RandomAdlibAnswerIntent'
    session.attributes['adlib-artist'] = artist_name

    return question(adlib_quiz_msg).reprompt(adlib_quiz_msg).simple_card(
        title="Guess The Random Artist Adlib", content="Who is it?")


@ask.intent('RandomAdlibAnswerIntent', mapping={'artist': 'Artist'})
def answer(artist):

    if artist is None or len(artist) <= 0:
        msg = 'Your guess did not include an artist'
        card_text = 'Your guess did not include an artist'
    else:
        # Checks if answer is correct or a synonym for correct answer
        print('Random answer', artist)
        artist = artist.title()
        found, artist = format_artist_synonyms(artist)
        print('Random answer after synonym', artist)

        # The persisted random_artist from 'RandomAdlibIntent'
        winning_answer = session.attributes['adlib-artist']

        # If they got it right, say yes. If not, tell em who it is.
        if found == True and winning_answer == artist:
            msg = "Correct!"
            card_text = "Right!"
        else:
            msg = '<speak><audio src="https://s3.amazonaws.com/rap-adlibs/WRONGANSWER.mp3" /> <break time="500ms" /> it was {}</speak>'.format(
                winning_answer)
            card_text = "Wrong:("

    return statement(msg).simple_card(
        title="And your guess is...", content=card_text)


@ask.intent('DoYouHaveIntent', mapping={'artist': 'Artist'})
def next_round(artist):

    if artist is None or len(artist) <= 0:
        msg = 'You did not give me a valid artist'
        card_text = 'You did not give me a valid artist'
    else:
        # Takes the artist the user asks for,
        # returns whether we have them or not (found)
        artist = artist.title()
        response = get_specific_artist(artist, artists_names_list, adlibs)
        found = response[0]

        if found == True:
            adlib_artist = response[1]
            adlib_audio_url = response[2]
            card_text = "I do have adlibs for {}!".format(artist)
            msg = "<speak>Yeah, I have adlibs for {}, here's one <break time='500ms' /><audio src='{}' /> <break time='500ms' /></speak>".format(
                artist, adlib_audio_url)
        elif found == False:
            card_text = "I don't have that artist, sorry."
            msg = "<speak>I don't have that artist, sorry.</speak>"

    return statement(msg).simple_card(title="Do I Have", content=card_text)


@ask.intent('WhoDoYouHaveIntent')
def next_round():
    artists_names_sentence = ", ".join(artists_names_list)
    msg = '<speak>I have adlibs for {}</speak>'.format(artists_names_sentence)
    card_text = 'I have adlibs for {}'.format(artists_names_sentence)
    return statement(msg).simple_card(
        title="Who Do You Have", content=card_text)


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
