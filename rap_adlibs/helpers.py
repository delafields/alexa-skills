from artist_data import artists_names_synonyms, artists_names_list
from random import randint


def get_random_adlib(artists_names_list, adlibs):
    # gets a random artist from the artists_names_list
    random_idx = randint(0, len(artists_names_list) - 1)
    random_artist_name = artists_names_list[random_idx]

    num_adlibs = len(adlibs[random_artist_name])
    if num_adlibs > 1:
        # chooses a random adlib from random_artist_name
        random_adlib = adlibs[random_artist_name][randint(0, num_adlibs - 1)]
    else:
        # chooses the single adlib available
        random_adlib = adlibs[random_artist_name][0]

    return random_artist_name, random_adlib


def format_artist_synonyms(artist_name):

    artist_name = artist_name.lower()
    found = False
    synonyms = artists_names_synonyms

    # Simple if-else chain to see if the synonym belongs to an artist,
    # If the synonym doesn't match anything, found = False
    if artist_name in synonyms["rick ross"]:
        artist_name = "rick ross"
        found = True
    elif artist_name in synonyms["2 chains"]:
        artist_name = "2 chains"
        found = True
    elif artist_name in synonyms["quavo"]:
        artist_name = "quavo"
        found = True
    elif artist_name in synonyms["gucci mane"]:
        artist_name = "gucci mane"
        found = True
    elif artist_name in synonyms["travis scott"]:
        artist_name = "travis scott"
        found = True
    elif artist_name in synonyms["offset"]:
        artist_name = "offset"
        found = True
    elif artist_name in synonyms["metro boomin"]:
        artist_name = "metro boomin"
        found = True
    elif artist_name in synonyms["kanye west"]:
        artist_name = "kanye west"
        found = True
    elif artist_name in synonyms["chance the rapper"]:
        artist_name = "chance the rapper"
        found = True
    else:
        found = False

    return (found, artist_name)


def get_specific_artist(artist, artists_names_list, adlibs):

    # returns the name of the artist after checking synonyms
    artist = artist.lower()
    found, artist_name = format_artist_synonyms(artist)

    # If we have the artist, retrieve the name & adlib url
    if found == True:

        num_adlibs = len(adlibs[artist_name])

        if num_adlibs > 1:
            artist_adlib = adlibs[artist_name][randint(0, num_adlibs - 1)]

        else:
            artist_adlib = adlibs[artist_name][0]

        return [found, artist_name, artist_adlib]
    else:
        return [found]


def have_adlibs_for(artist, artists_names_list):
    # returns the name of the artist after checking synonyms
    artist = artist.lower()
    found, artist_name = format_artist_synonyms(artist)

    return found
