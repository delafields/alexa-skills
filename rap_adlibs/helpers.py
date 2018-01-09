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

    found = False
    synonyms = artists_names_synonyms

    # Simple if-else chain to see if the synonym belongs to an artist,
    # If the synonym doesn't match anything, found = False
    if artist_name in synonyms["Action Bronson"]:
        artist_name = "Action Bronson"
        found = True
    elif artist_name in synonyms["Akon"]:
        artist_name = "Akon"
        found = True
    elif artist_name in synonyms["Big Boi"]:
        artist_name = "Big Boi"
        found = True
    elif artist_name in synonyms["Biggie Smalls"]:
        artist_name = "Biggie Smalls"
        found = True
    elif artist_name in synonyms["Big Sean"]:
        artist_name = "Big Sean"
        found = True
    elif artist_name in synonyms["Birdman"]:
        artist_name = "Birdman"
        found = True
    elif artist_name in synonyms["Bobby Shmurda"]:
        artist_name = "Bobby Shmurda"
        found = True
    elif artist_name in synonyms["Bun B"]:
        artist_name = "Bun B"
        found = True
    elif artist_name in synonyms["Busta Rhymes"]:
        artist_name = "Busta Rhymes"
        found = True
    elif artist_name in synonyms["Camron"]:
        artist_name = "Camron"
        found = True
    elif artist_name in synonyms["Chance The Rapper"]:
        artist_name = "Chance"
        found = True
    elif artist_name in synonyms["Chief Keef"]:
        artist_name = "Chief Keef"
        found = True
    elif artist_name in synonyms["Chingy"]:
        artist_name = "Chingy"
        found = True
    elif artist_name in synonyms["Currensy"]:
        artist_name = "Currensy"
        found = True
    elif artist_name in synonyms["Danny Brown"]:
        artist_name = "Danny Brown"
        found = True
    elif artist_name in synonyms["Designer"]:
        artist_name = "Designer"
        found = True
    elif artist_name in synonyms["DJ Drama"]:
        artist_name = "DJ Drama"
        found = True
    elif artist_name in synonyms["DJ Khaled"]:
        artist_name = "DJ Khaled"
        found = True
    elif artist_name in synonyms["DJ Mustard"]:
        artist_name = "DJ Mustard"
        found = True
    elif artist_name in synonyms["DJ Paul"]:
        artist_name = "DJ Paul"
        found = True
    elif artist_name in synonyms["DMX"]:
        artist_name = "DMX"
        found = True
    elif artist_name in synonyms["Drake"]:
        artist_name = "Drake"
        found = True
    elif artist_name in synonyms["E 40"]:
        artist_name = "E 40"
        found = True
    elif artist_name in synonyms["Eminem"]:
        artist_name = "Eminem"
        found = True
    elif artist_name in synonyms["Fat Joe"]:
        artist_name = "Fat Joe"
        found = True
    elif artist_name in synonyms["Fetty Wap"]:
        artist_name = "Fetty Wap"
        found = True
    elif artist_name in synonyms["French Montana"]:
        artist_name = "French Montana"
        found = True
    elif artist_name in synonyms["Future"]:
        artist_name = "Future"
        found = True
    elif artist_name in synonyms["Gucci Mane"]:
        artist_name = "Gucci Mane"
        found = True
    elif artist_name in synonyms["Hurricane Chris"]:
        artist_name = "Hurricane Chris"
        found = True
    elif artist_name in synonyms["Jadakiss"]:
        artist_name = "Jadakiss"
        found = True
    elif artist_name in synonyms["Ja Rule"]:
        artist_name = "Ja Rule"
        found = True
    elif artist_name in synonyms["Jay Z"]:
        artist_name = "Jay Z"
        found = True
    elif artist_name in synonyms["J Cole"]:
        artist_name = "J Cole"
        found = True
    elif artist_name in synonyms["Jim Jones"]:
        artist_name = "Jim Jones"
        found = True
    elif artist_name in synonyms["Juelz Santana"]:
        artist_name = "Juelz Santana"
        found = True
    elif artist_name in synonyms["Juicy J"]:
        artist_name = "Juicy J"
        found = True
    elif artist_name in synonyms["Kanye West"]:
        artist_name = "Kanye West"
        found = True
    elif artist_name in synonyms["Kendrick Lamar"]:
        artist_name = "Kendrick Lamar"
        found = True
    elif artist_name in synonyms["Killa Mike"]:
        artist_name = "Killa Mike"
        found = True
    elif artist_name in synonyms["Lil B"]:
        artist_name = "Lil B"
        found = True
    elif artist_name in synonyms["Lil Jon"]:
        artist_name = "Lil Jon"
        found = True
    elif artist_name in synonyms["Lil Kim"]:
        artist_name = "Lil Kim"
        found = True
    elif artist_name in synonyms["Lil Pump"]:
        artist_name = "Lil Pump"
        found = True
    elif artist_name in synonyms["Lil Scrappy"]:
        artist_name = "Lil Scrappy"
        found = True
    elif artist_name in synonyms["Lil Uzi Vert"]:
        artist_name = "Lil Uzi Vert"
        found = True
    elif artist_name in synonyms["Lil Wayne"]:
        artist_name = "Lil Wayne"
        found = True
    elif artist_name in synonyms["Lil Yachty"]:
        artist_name = "Lil Yachty"
        found = True
    elif artist_name in synonyms["Lloyd Banks"]:
        artist_name = "Lloyd Banks"
        found = True
    elif artist_name in synonyms["Ludacris"]:
        artist_name = "Ludacris"
        found = True
    elif artist_name in synonyms["Made in Tyo"]:
        artist_name = "Made in Tyo"
        found = True
    elif artist_name in synonyms["Mannie Fresh"]:
        artist_name = "Mannie Fresh"
        found = True
    elif artist_name in synonyms["Meek Mill"]:
        artist_name = "Meek Mill"
        found = True
    elif artist_name in synonyms["Metro Boomin"]:
        artist_name = "Metro Boomin"
        found = True
    elif artist_name in synonyms["Migos"]:
        artist_name = "Migos"
        found = True
    elif artist_name in synonyms["Mike Jones"]:
        artist_name = "Mike Jones"
        found = True
    elif artist_name in synonyms["Nas"]:
        artist_name = "Nas"
        found = True
    elif artist_name in synonyms["Nate Dogg"]:
        artist_name = "Nate Dogg"
        found = True
    elif artist_name in synonyms["Nicki Minaj"]:
        artist_name = "Nicki Minaj"
        found = True
    elif artist_name in synonyms["ODB"]:
        artist_name = "ODB"
        found = True
    elif artist_name in synonyms["OJ Da Juiceman"]:
        artist_name = "OJ Da Juiceman"
        found = True
    elif artist_name in synonyms["P Diddy"]:
        artist_name = "P Diddy"
        found = True
    elif artist_name in synonyms["Pharrell"]:
        artist_name = "Pharrell"
        found = True
    elif artist_name in synonyms["Pimp C"]:
        artist_name = "Pimp C"
        found = True
    elif artist_name in synonyms["Pitbull"]:
        artist_name = "Pitbull"
        found = True
    elif artist_name in synonyms["Project Pat"]:
        artist_name = "Project Pat"
        found = True
    elif artist_name in synonyms["Pusha T"]:
        artist_name = "Pusha T"
        found = True
    elif artist_name in synonyms["Quavo"]:
        artist_name = "Quavo"
        found = True
    elif artist_name in synonyms["Rae Sremmurd"]:
        artist_name = "Rae Sremmurd"
        found = True
    elif artist_name in synonyms["Rick Ross"]:
        artist_name = "Rick Ross"
        found = True
    elif artist_name in synonyms["Schoolboy Q"]:
        artist_name = "Schoolboy Q"
        found = True
    elif artist_name in synonyms["Slim Thug"]:
        artist_name = "Slim Thug"
        found = True
    elif artist_name in synonyms["Snoop Dogg"]:
        artist_name = "Snoop Dogg"
        found = True
    elif artist_name in synonyms["Soulja Boy"]:
        artist_name = "Soulja Boy"
        found = True
    elif artist_name in synonyms["Swizz Beatz"]:
        artist_name = "Swizz Beatz"
        found = True
    elif artist_name in synonyms["Takeoff"]:
        artist_name = "Takeoff"
        found = True
    elif artist_name in synonyms["T I"]:
        artist_name = "T I"
        found = True
    elif artist_name in synonyms["T Pain"]:
        artist_name = "T Pain"
        found = True
    elif artist_name in synonyms["Trapaholics"]:
        artist_name = "Trapaholics"
        found = True
    elif artist_name in synonyms["Travis Scott"]:
        artist_name = "Travis Scott"
        found = True
    elif artist_name in synonyms["Trick Daddy"]:
        artist_name = "Trick Daddy"
        found = True
    elif artist_name in synonyms["Tupac"]:
        artist_name = "Tupac"
        found = True
    elif artist_name in synonyms["Tyga"]:
        artist_name = "Tyga"
        found = True
    elif artist_name in synonyms["Waka Flocka Flame"]:
        artist_name = "Waka Flocka Flame"
        found = True
    elif artist_name in synonyms["Wiz Khalifa"]:
        artist_name = "Wiz Khalifa"
        found = True
    elif artist_name in synonyms["Ying Yang Twins"]:
        artist_name = "Ying Yang Twins"
        found = True
    elif artist_name in synonyms["Young Jeezy"]:
        artist_name = "Young Jeezy"
        found = True
    elif artist_name in synonyms["Young Thug"]:
        artist_name = "Young Thug"
        found = True
    elif artist_name in synonyms["2 Chainz"]:
        artist_name = "2 Chainz"
        found = True
    elif artist_name in synonyms["21 Savage"]:
        artist_name = "21 Savage"
        found = True
    elif artist_name in synonyms["3 6 Mafia"]:
        artist_name = "3 6 Mafia"
        found = True
    elif artist_name in synonyms["50 Cent"]:
        artist_name = "50 Cent"
        found = True
    else:
        found = False

    return (found, artist_name)


def get_specific_artist(artist, artists_names_list, adlibs):

    # returns the name of the artist after checking synonyms
    # Removing artist = artist.lower()
    print(artist)
    found, artist_name = format_artist_synonyms(artist)
    print(artist_name)

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
