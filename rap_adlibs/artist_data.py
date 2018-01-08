artists_names_list = [
    "Action Bronson",
    "Akon",
    "Big Boi",
    "Biggie Smalls",
    "Big Sean",
    "Birdman",
    "Bobby Shmurda",
    "Bun B",
    "Busta Rhymes",
    "Camron",
    "Chance The Rapper",
    "Chief Keef",
    "Chingy",
    "Currensy",
    "Danny Brown",
    "Designer",
    "DJ Drama",
    "DJ Khaled",
    "DJ Mustard",
    "DJ Paul",
    "DMX",
    "Drake",
    "E 40",
    "Eminem",
    "Fat Joe",
    "Fetty Wap",
    "French Montana",
    "Future",
    "Gucci Mane",
    "Hurricane Chris",
    "Jadakiss",
    "Ja Rule",
    "Jay Z",
    "J Cole",
    "Jim Jones",
    "Juelz Santana",
    "Juicy J",
    "Kanye West",
    "Kendrick Lamar",
    "Killa Mike",
    "Lil B",
    "Lil Jon",
    "Lil Kim",
    "Lil Pump",
    "Lil Scrappy",
    "Lil Uzi Vert",
    "Lil Wayne",
    "Lil Yachty",
    "Lloyd Banks",
    "Ludacris",
    "Made in Tyo",
    "Mannie Fresh",
    "Meek Mill",
    "Metro Boomin",
    "Migos",
    "Mike Jones",
    "Nas",
    "Nate Dogg",
    "Nicki Minaj",
    "ODB",
    "OJ Da Juiceman",
    "P Diddy",
    "Pharrell",
    "Pimp C",
    "Pitbull",
    "Project Pat",
    "Pusha T",
    "Quavo",
    "Rae Sremmurd",
    "Rick Ross",
    "Schoolboy Q",
    "Slim Thug",
    "Snoop Dogg",
    "Soulja Boy",
    "Swizz Beatz",
    "Takeoff",
    "T I",
    "T Pain",
    "Trapaholics",
    "Travis Scott",
    "Trick Daddy",
    "Tupac",
    "Tyga",
    "Waka Flocka Flame",
    "Wiz Khalifa",
    "Ying Yang Twins",
    "Young Jeezy",
    "Young Thug",
    "2 Chainz",
    "21 Savage",
    "3 6 Mafia"
    "50 Cent",
]

# synonyms keys are values for the ARTIST_NAME slot type
# each key has an array of pseudonyms/synonyms for each artist
# *** make sure the array has the actual slot value ***
artists_names_synonyms = {
    "Action Bronson": ["Action Bronson", "Bronson", "Action"],
    "Akon": ["Akon"],
    "Big Boi": ["Big Boi", "Big Boy", "Daddy Fat Stacks"],
    "Biggie Smalls":
    ["Biggie Smalls", "Notorious B I G", "Biggie", "Biggy", "Biggy Smalls"],
    "Big Sean": ["Big Sean", "Sean Don"],
    "Birdman": [
        "Birdman", "Stunna", "Stunner", "Number One Stunna",
        "Number One Stunner", "Number One Stunter", "Number One Stunter"
    ],
    "Bobby Shmurda":
    ["Bobby Shmurda", "Bobby Shmurder", "Bobby Murder", "Bobby Murda"],
    "Bun B": ["Bun B", "Bun", "Trill OG"],
    "Busta Rhymes": ["Busta Rhymes", "Buster Rhymes", "Busta", "Buster"],
    "Camron": ["Camron", "Cam Ron", "Cam", "Killa Cam", "Killer Cam"],
    "Chance The Rapper": ["Chance The Rapper", "Chance Tha Rapper", "Chance"],
    "Chief Keef": ["Chief Keef", "Chief", "Keef"],
    "Chingy": ["Chingy"],
    "Currensy": ["Currensy"],
    "Danny Brown": ["Danny Brown", "Dan Brown"],
    "Designer": ["Designer", "Panda Guy", "Panda"],
    "DJ Drama": ["DJ Drama", "Drama"],
    "DJ Khaled": ["DJ Khaled", "Khaled"],
    "DJ Mustard": ["DJ Mustard", "Mustard"],
    "DJ Paul": ["DJ Paul", "Paul"],
    "DMX": ["DMX", "D M X"],
    "Drake": ["Drake", "Drizzy", "Aubrey", "Aubrey Graham", "Champagne Papi"],
    "E 40": ["E 40", "E40", "E Forty"],
    "Eminem":
    ["Eminem", "Em", "Slim", "Slim Shady", "Marshall", "Marshall Mathers"],
    "Fat Joe": ["Fat Joe", "Joe"],
    "Fetty Wap": ["Fetty Wap", "Fetty"],
    "French Montana": ["French Montana", "French"],
    "Future": ["Future", "Hendrix", "Hendricks"],
    "Gucci Mane": [
        "Gucci Mane", "Gucci", "Gucci Man", "Radric", "Radric Davis"
    ],
    "Hurricane Chris": ["Hurricane Chris"],
    "Jadakiss": ["Jadakiss", "Jada"],
    "Ja Rule": ["Ja Rule"],
    "Jay Z": ["Jay Z", "Jay", "Hov", "Hova"],
    "J Cole": ["J Cole", "Cole", "Cole World"],
    "Jim Jones": ["Jim Jones"],
    "Juelz Santana": ["Juelz Santana", "Juelz", "Santana"],
    "Juicy J": ["Juicy J", "Juicy"],
    "Kanye West": [
        "Kanye West", "Kanye", "Yeezy", "Yeezus", "The Goat", "The Old Kanye"
    ],
    "Kendrick Lamar": [
        "Kendrick Lamar", "Kendrick", "Kenny", "Cornrow Kenny", "Lamar"
    ],
    "Killa Mike": ["Killa Mike", "Killer Mike"],
    "Lil B": ["Lil B", "Based God", "Base God"],
    "Lil Jon": ["Lil Jon", "Lil John", "Little Jon", "Little John"],
    "Lil Kim": ["Lil Kim", "Little Kim", "Kim", "Queen Bee"],
    "Lil Pump": ["Lil Pump", "Pump"],
    "Lil Scrappy": ["Lil Scrappy", "Scrappy"],
    "Lil Uzi Vert": [
        "Lil Uzi Vert", "Lil Uzi", "Little Uzi Vert", "Little Uzi", "Uzi",
        "Uzi Vert"
    ],
    "Lil Wayne":
    ["Lil Wayne", "Little Wayne", "Wayne", "Weezy", "Weezy F", "Weezy F Baby"],
    "Lil Yachty": [
        "Lil Yachty", "Little Yachty", "Yachty", "Lil Boat", "Litle Boat"
    ],
    "Lloyd Banks": ["Lloyd Banks", "Lloyd", "Banks"],
    "Ludacris": ["Ludacris", "Ludicrous", "Luda"],
    "Made in Tyo": ["Made In Tyo", "Made In T O"],
    "Mannie Fresh": ["Mannie Fresh", "Mannie"],
    "Meek Mill": ["Meek Mill", "Meek", "Mill"],
    "Metro Boomin": [
        "Metro Boomin", "Metro Booming"
        "Metro", "Young Metro", "Boomin"
    ],
    "Migos": [
        "Migos", "Migo", "Takeoff", "Take Off", "Offset", "Off Set", "Quavo"
    ],
    "Mike Jones": ["Mike Jones"],
    "Nas": ["Nas", "Nastradamus", "Nostradamus"],
    "Nate Dogg": ["Nate Dogg", "Nate Dog"],
    "Nicki Minaj": ["Nicki Minaj", "Nicki Menage", "Nicki", "Minaj", "Menage"],
    "ODB": ["ODB", "Old Dirty Bastard"],
    "OJ Da Juiceman": ["OJ Da Juiceman", "OJ", "O J"],
    "P Diddy": ["P Diddy", "Diddy", "Puff", "Puff Daddy"],
    "Pharrell": ["Pharrell", "Skateboard P", "P", "Ferrell"],
    "Pimp C": ["Pimp C", "Sweet Jones"],
    "Pitbull": ["Pitbull", "Mr. Worldwide", "Mr 305"],
    "Project Pat": ["Project Pat"],
    "Pusha T": ["Pusha T"],
    "Quavo": ["Quavo"],
    "Rae Sremmurd": ["Rae Sremmurd", "Rae", "Ray Sremmurd", "Ray"],
    "Rick Ross": [
        "Rick Ross", "Ricky Ross", "The Boss", "The Boss Rick Ross",
        "The Boss Ricky Ross"
    ],
    "Schoolboy Q": ["Schoolboy Q", "Schoolboy", "Q"],
    "Slim Thug": ["Slim Thug", "Slim Thugga", "Slim Thugger"],
    "Snoop Dogg": [
        "Snoop Dogg", "Snoop Dog", "Snoop D O Double G", "D O Double G"
    ],
    "Soulja Boy": ["Soulja Boy", "Soldier Boy", "Soulja", "Soldier"],
    "Swizz Beatz": [
        "Swizz Beatz", "Swizz Beats", "Swiss Beatz", "Swiss Beats"
    ],
    "Takeoff": ["Takeoff", "Take Off"],
    "T I": ["T I", "TIP"],
    "T Pain": ["T Pain"],
    "Trapaholics": ["Trapaholics", "DJ Trapaholics"],
    "Travis Scott": ["Travis Scott", "Travis", "Scott", "La Flame"],
    "Trick Daddy": ["Trick Daddy", "Trick"],
    "Tupac": ["Tupac", "Tupack", "Pac", "Pack"],
    "Tyga": ["Tyga"],
    "Waka Flocka Flame": [
        "Waka Flocka Flame", "Waka", "Wocka", "Wocka Flocka Flame", "Flocka"
    ],
    "Wiz Khalifa": ["Wiz Khalifa", "Wiz", "Khalifa"],
    "Ying Yang Twins": ["Ying Yang Twins", "Ying Yang Twinz", "Ying Yang"],
    "Young Jeezy": ["Young Jeezy", "Jeezy"],
    "Young Thug": ["Young Thug", "Thugga", "Thugger", "Thugga"],
    "2 Chainz": [
        "2 Chainz", "2 Chains", "Two Chainz", "Two Chains", "Titty Boy"
    ],
    "21 Savage": ["21 Savage", "21", "Savage"],
    "3 6 Mafia": ["3 6 Mafia", "3 6", "Three Six"],
    "50 Cent": ["50 Cent", "50", "Fifty Cent", "Fifty"],
}

adlibs = {
    "rick ross": [
        "https://s3.amazonaws.com/ask-storage/tidePooler/OceanWaves.mp3",
        "https://s3.amazonaws.com/ask-storage/tidePooler/OceanWaves.mp3"
    ],
    "2 chains":
    ["https://s3.amazonaws.com/ask-storage/tidePooler/OceanWaves.mp3"],
    "quavo":
    ["https://s3.amazonaws.com/ask-storage/tidePooler/OceanWaves.mp3"],
    "gucci mane":
    ["https://s3.amazonaws.com/ask-storage/tidePooler/OceanWaves.mp3"],
    "travis scott": [
        "https://s3.amazonaws.com/ask-storage/tidePooler/OceanWaves.mp3"
    ],
    "offset": [
        "https://s3.amazonaws.com/ask-storage/tidePooler/OceanWaves.mp3"
    ],
    "metro boomin": [
        "https://s3.amazonaws.com/ask-storage/tidePooler/OceanWaves.mp3"
    ],
    "kanye west": [
        "https://s3.amazonaws.com/ask-storage/tidePooler/OceanWaves.mp3"
    ],
    "chance the rapper": [
        "https://s3.amazonaws.com/ask-storage/tidePooler/OceanWaves.mp3"
    ]
}
