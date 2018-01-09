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
    "3 6 Mafia",
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
    "Action Bronson": [
        "https://s3.amazonaws.com/rap-adlibs/ActionBronson_brosolino.mp3",
        "https://s3.amazonaws.com/rap-adlibs/ActionBronson_various.mp3"
    ],
    "Akon": ["https://s3.amazonaws.com/rap-adlibs/Akon_konvictMusic.mp3"],
    "Big Boi": ["https://s3.amazonaws.com/rap-adlibs/BigBoi_boiStop.mp3"],
    "Biggie Smalls": [
        "https://s3.amazonaws.com/rap-adlibs/BiggieSmalls_babyBaby.mp3",
        "https://s3.amazonaws.com/rap-adlibs/BiggieSmalls_uhh.mp3"
    ],
    "Big Sean": [
        "https://s3.amazonaws.com/rap-adlibs/BigSean_boiDoIt.mp3",
        "https://s3.amazonaws.com/rap-adlibs/BigSean_various1.mp3",
        "https://s3.amazonaws.com/rap-adlibs/BigSean_various2.mp3"
    ],
    "Birdman": [
        "https://s3.amazonaws.com/rap-adlibs/Birdman_birdcall.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Birdman_brrr.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Birdman_putSomeRespek.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Birdman_various1.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Birdman_various2.mp3"
    ],
    "Bobby Shmurda":
    ["https://s3.amazonaws.com/rap-adlibs/BobbyShmurda_ahAhAh.mp3"],
    "Bun B": ["https://s3.amazonaws.com/rap-adlibs/BunB_UGKForLife.mp3"],
    "Busta Rhymes": [
        "https://s3.amazonaws.com/rap-adlibs/BustaRhymes_laugh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/BustaRhymes_yahyahyah.mp3"
    ],
    "Camron": ["https://s3.amazonaws.com/rap-adlibs/Camron_various1.mp3"],
    "Chance The Rapper":
    ["https://s3.amazonaws.com/rap-adlibs/ChanceTheRapper_aah.mp3"],
    "Chief Keef":
    ["https://s3.amazonaws.com/rap-adlibs/ChiefKeef_bangBang.mp3"],
    "Chingy": ["https://s3.amazonaws.com/rap-adlibs/Chingy_rightThurr.mp3"],
    "Currensy": ["https://s3.amazonaws.com/rap-adlibs/Currensy_jetLife.mp3"],
    "Danny Brown": [
        "https://s3.amazonaws.com/rap-adlibs/DannyBrown_laugh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/DannyBrown_various1.mp3"
    ],
    "Designer": [
        "https://s3.amazonaws.com/rap-adlibs/Desiigner_fsdhjklf.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Desiigner_panda.mp3"
    ],
    "DJ Drama": ["https://s3.amazonaws.com/rap-adlibs/DJDrama.mp3"],
    "DJ Khaled": [
        "https://s3.amazonaws.com/rap-adlibs/DJKhaled_djKhaled.mp3",
        "https://s3.amazonaws.com/rap-adlibs/DJKhaled_forThaHood.mp3",
        "https://s3.amazonaws.com/rap-adlibs/DJKhaled_various1.mp3",
        "https://s3.amazonaws.com/rap-adlibs/DJKhaled_various2.mp3",
        "https://s3.amazonaws.com/rap-adlibs/DJKhaled_various3.mp3"
    ],
    "DJ Mustard": ["https://s3.amazonaws.com/rap-adlibs/DJMustard.mp3"],
    "DJ Paul": ["https://s3.amazonaws.com/rap-adlibs/DJPaul_various.mp3"],
    "DMX": [
        "https://s3.amazonaws.com/rap-adlibs/DMX_cmon.mp3",
        "https://s3.amazonaws.com/rap-adlibs/DMX_grrBark.mp3",
        "https://s3.amazonaws.com/rap-adlibs/DMX_uhh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/DMX_yeah.mp3"
    ],
    "Drake": [
        "https://s3.amazonaws.com/rap-adlibs/Drake_alright.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Drake_godDamn.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Drake_uhh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Drake_worst.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Drake_yeah.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Drake_yeahYeah.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Drake_youngMoney.mp3"
    ],
    "E 40": [
        "https://s3.amazonaws.com/rap-adlibs/E40_eouh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/E40_ghostRideDaWhip.mp3"
    ],
    "Eminem": [
        "https://s3.amazonaws.com/rap-adlibs/Eminem_myNameIs.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Eminem_slimShady.mp3"
    ],
    "Fat Joe": [
        "https://s3.amazonaws.com/rap-adlibs/FatJoe_crack.mp3",
        "https://s3.amazonaws.com/rap-adlibs/FatJoe_oww.mp3"
    ],
    "Fetty Wap": [
        "https://s3.amazonaws.com/rap-adlibs/FettyWap_1738.mp3",
        "https://s3.amazonaws.com/rap-adlibs/FettyWap_ayYahBaby.mp3"
    ],
    "French Montana": [
        "https://s3.amazonaws.com/rap-adlibs/FrenchMontana_haan.mp3",
        "https://s3.amazonaws.com/rap-adlibs/FrenchMontana_montana.mp3"
    ],
    "Future": [
        "https://s3.amazonaws.com/rap-adlibs/Future_brrStickEm.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Future_hendrix.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Future_wooh.mp3"
    ],
    "Gucci Mane": [
        "https://s3.amazonaws.com/rap-adlibs/GucciMane_burr.mp3",
        "https://s3.amazonaws.com/rap-adlibs/GucciMane_damn.mp3",
        "https://s3.amazonaws.com/rap-adlibs/GucciMane_itsGucci.mp3",
        "https://s3.amazonaws.com/rap-adlibs/GucciMane_yeuh.mp3"
    ],
    "Hurricane Chris": [
        "https://s3.amazonaws.com/rap-adlibs/HurricaneChris_ayBaby.mp3"
    ],
    "Jadakiss": ["https://s3.amazonaws.com/rap-adlibs/Jadakiss_aha.mp3"],
    "Ja Rule": [
        "https://s3.amazonaws.com/rap-adlibs/JaRule_hollaHolla.mp3",
        "https://s3.amazonaws.com/rap-adlibs/JaRule_itsMurda.mp3"
    ],
    "Jay Z": [
        "https://s3.amazonaws.com/rap-adlibs/JayZ_hovChyeah.mp3",
        "https://s3.amazonaws.com/rap-adlibs/JayZ_JiggaMan.mp3",
        "https://s3.amazonaws.com/rap-adlibs/JayZ_uhuhuh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/JayZ_various1.mp3",
        "https://s3.amazonaws.com/rap-adlibs/JayZ_various2.mp3",
        "https://s3.amazonaws.com/rap-adlibs/JayZ_yessir.mp3",
        "https://s3.amazonaws.com/rap-adlibs/JayZ_yo.mp3"
    ],
    "J Cole": ["https://s3.amazonaws.com/rap-adlibs/JCole_biyitch.mp3"],
    "Jim Jones": ["https://s3.amazonaws.com/rap-adlibs/JimJones_various1.mp3"],
    "Juelz Santana": [
        "https://s3.amazonaws.com/rap-adlibs/JuelzSantana_aye.mp3"
    ],
    "Juicy J": ["https://s3.amazonaws.com/rap-adlibs/JuicyJ_various2.mp3"],
    "Kanye West": [
        "https://s3.amazonaws.com/rap-adlibs/Kanye_uh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Kanye_uhuh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Kanye_wooh.mp3"
    ],
    "Kendrick Lamar": [
        "https://s3.amazonaws.com/rap-adlibs/KendrickLamar_biyatch.mp3",
        "https://s3.amazonaws.com/rap-adlibs/KendrickLamar_dodododo.mp3"
    ],
    "Killa Mike": [
        "https://s3.amazonaws.com/rap-adlibs/KillaMike_crimeTimeRapGame.mp3"
    ],
    "Lil B": ["https://s3.amazonaws.com/rap-adlibs/LilB_swag.mp3"],
    "Lil Jon": [
        "https://s3.amazonaws.com/rap-adlibs/LilJon_okay.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LilJon_what.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LilJon_whatsHappenin.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LilJon_yeah.mp3"
    ],
    "Lil Kim": ["https://s3.amazonaws.com/rap-adlibs/LilKim_queenBee.mp3"],
    "Lil Pump": [
        "https://s3.amazonaws.com/rap-adlibs/LilPump_Esketit.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LilPump_ooh.mp3"
    ],
    "Lil Scrappy": [
        "https://s3.amazonaws.com/rap-adlibs/LilScrappy_okaykaykay.mp3"
    ],
    "Lil Uzi Vert": [
        "https://s3.amazonaws.com/rap-adlibs/LilUziVert_yeuh.mp3"
    ],
    "Lil Wayne": [
        "https://s3.amazonaws.com/rap-adlibs/LilWayne_damn.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LilWayne_datRight.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LilWayne_hitMe.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LilWayne_various1.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LilWayne_various2.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LilWayne_various3.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LilWayne_whatItIs.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LilWayne_youngMoolaBaby.mp3"
    ],
    "Lil Yachty": [
        "https://s3.amazonaws.com/rap-adlibs/LilYachty_lilBoat.mp3"
    ],
    "Lloyd Banks": [
        "https://s3.amazonaws.com/rap-adlibs/LloydBanks_uhh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/LloydBanks_yeah.mp3"
    ],
    "Ludacris": ["https://s3.amazonaws.com/rap-adlibs/Ludacris_luda.mp3"],
    "Made in Tyo": [
        "https://s3.amazonaws.com/rap-adlibs/MadeInTyo_skrtskrt.mp3"
    ],
    "Mannie Fresh": [
        "https://s3.amazonaws.com/rap-adlibs/MannieFresh_frefreFresh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/MannieFresh_ladiesAndGentlemen.mp3"
    ],
    "Meek Mill": [
        "https://s3.amazonaws.com/rap-adlibs/MeekMill_blahblah.mp3",
        "https://s3.amazonaws.com/rap-adlibs/MeekMill_uhh.mp3"
    ],
    "Metro Boomin": [
        "https://s3.amazonaws.com/rap-adlibs/MetroBoomin_wantsSomeMore.mp3"
    ],
    "Migos": [
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_aye.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_ayeTakeoff.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_damn.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_grah.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_money.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_uhh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Quavo_gone.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Quavo_hey.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Quavo_MAMA.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Quavo_migos.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Quavo_yeuck.mp3"
    ],
    "Mike Jones": [
        "https://s3.amazonaws.com/rap-adlibs/MikeJones_chyeah.mp3",
        "https://s3.amazonaws.com/rap-adlibs/MikeJones_iceAge.mp3",
        "https://s3.amazonaws.com/rap-adlibs/MikeJones_mikeJones.mp3"
    ],
    "Nas": ["https://s3.amazonaws.com/rap-adlibs/Nas_various1.mp3"],
    "Nate Dogg": ["https://s3.amazonaws.com/rap-adlibs/NateDogg_holdUp.mp3"],
    "Nicki Minaj": [
        "https://s3.amazonaws.com/rap-adlibs/NickiMinaj_various1.mp3",
        "https://s3.amazonaws.com/rap-adlibs/NickiMinaj_various2.mp3",
        "https://s3.amazonaws.com/rap-adlibs/NickiMinaj_various3.mp3"
    ],
    "ODB": ["https://s3.amazonaws.com/rap-adlibs/ODB_shimmyYa.mp3"],
    "OJ Da Juiceman": [
        "https://s3.amazonaws.com/rap-adlibs/OjDaJuiceman_aye.mp3"
    ],
    "P Diddy": [
        "https://s3.amazonaws.com/rap-adlibs/PDiddy_various1.mp3",
        "https://s3.amazonaws.com/rap-adlibs/PDiddy_various2.mp3"
    ],
    "Pharrell": ["https://s3.amazonaws.com/rap-adlibs/Pharrell_yezzir.mp3"],
    "Pimp C": [
        "https://s3.amazonaws.com/rap-adlibs/PimpC_holUp.mp3",
        "https://s3.amazonaws.com/rap-adlibs/PimpC_smokeSomethin.mp3",
        "https://s3.amazonaws.com/rap-adlibs/PimpC_sweetJones.mp3"
    ],
    "Pitbull": [
        "https://s3.amazonaws.com/rap-adlibs/Pitbull_DALE.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Pitbull_mr305.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Pitbull_yeeoh.mp3"
    ],
    "Project Pat": [
        "https://s3.amazonaws.com/rap-adlibs/ProjectPat_goodGooglyMoogly.mp3"
    ],
    "Pusha T": ["https://s3.amazonaws.com/rap-adlibs/PushaT_yeuck.mp3"],
    "Quavo": [
        "https://s3.amazonaws.com/rap-adlibs/Quavo_gone.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Quavo_hey.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Quavo_MAMA.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Quavo_migos.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Quavo_yeuck.mp3"
    ],
    "Rae Sremmurd": [
        "https://s3.amazonaws.com/rap-adlibs/RaeSremmurd_hey.mp3"
    ],
    "Rick Ross": [
        "https://s3.amazonaws.com/rap-adlibs/RickRoss_bawse.mp3",
        "https://s3.amazonaws.com/rap-adlibs/RickRoss_rickyRoss.mp3",
        "https://s3.amazonaws.com/rap-adlibs/RickRoss_uhh.mp3"
    ],
    "Schoolboy Q": [
        "https://s3.amazonaws.com/rap-adlibs/SchoolboyQ_yakyakyak.mp3"
    ],
    "Slim Thug": [
        "https://s3.amazonaws.com/rap-adlibs/SlimThug_bossHogOutlaws.mp3",
        "https://s3.amazonaws.com/rap-adlibs/SlimThug_slimThugga.mp3"
    ],
    "Snoop Dogg": [
        "https://s3.amazonaws.com/rap-adlibs/SnoopDogg_bigSnoopDODub.mp3",
        "https://s3.amazonaws.com/rap-adlibs/SnoopDogg_bladauw.mp3",
        "https://s3.amazonaws.com/rap-adlibs/SnoopDogg_talmBout.mp3"
    ],
    "Soulja Boy": [
        "https://s3.amazonaws.com/rap-adlibs/SouljaBoy_souljer.mp3",
        "https://s3.amazonaws.com/rap-adlibs/SouljaBoy_tellEm.mp3",
        "https://s3.amazonaws.com/rap-adlibs/SouljaBoy_yoooh.mp3"
    ],
    "Swizz Beatz": [
        "https://s3.amazonaws.com/rap-adlibs/SwizzBeatz_godDamnit.mp3",
        "https://s3.amazonaws.com/rap-adlibs/SwizzBeatz_itsShowtime.mp3"
    ],
    "Takeoff": [
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_aye.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_ayeTakeoff.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_damn.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_grah.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_money.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Takeoff_uhh.mp3"
    ],
    "T I": [
        "https://s3.amazonaws.com/rap-adlibs/TI_aintReadyFaDis.mp3",
        "https://s3.amazonaws.com/rap-adlibs/TI_grandHustlePatna.mp3",
        "https://s3.amazonaws.com/rap-adlibs/TI_TIP.mp3",
        "https://s3.amazonaws.com/rap-adlibs/TI_various1.mp3"
    ],
    "T Pain": [
        "https://s3.amazonaws.com/rap-adlibs/TPain_hey.mp3",
        "https://s3.amazonaws.com/rap-adlibs/TPain_nappyBoy.mp3"
    ],
    "Trapaholics": [
        "https://s3.amazonaws.com/rap-adlibs/Trapaholics_damnSon.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Trapaholics_trapaholicsMixtapes.mp3"
    ],
    "Travis Scott": [
        "https://s3.amazonaws.com/rap-adlibs/TravisScott_laFlame.mp3",
        "https://s3.amazonaws.com/rap-adlibs/TravisScott_straightUp.mp3",
        "https://s3.amazonaws.com/rap-adlibs/TravisScott_yah.mp3"
    ],
    "Trick Daddy": [
        "https://s3.amazonaws.com/rap-adlibs/TrickDaddy_trickLuhDaKids.mp3",
        "https://s3.amazonaws.com/rap-adlibs/TrickDaddy_uhuhOkayWassup.mp3"
    ],
    "Tupac": [
        "https://s3.amazonaws.com/rap-adlibs/Tupac_babay.mp3",
        "https://s3.amazonaws.com/rap-adlibs/Tupac_thugLife.mp3"
    ],
    "Tyga": ["https://s3.amazonaws.com/rap-adlibs/Tyga_uhh.mp3"],
    "Waka Flocka Flame": [
        "https://s3.amazonaws.com/rap-adlibs/WakaFlocka_brickSquad.mp3",
        "https://s3.amazonaws.com/rap-adlibs/WakaFlocka_flocka.mp3"
    ],
    "Wiz Khalifa": [
        "https://s3.amazonaws.com/rap-adlibs/WizKhalifa_laugh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/WizKhalifa_uhh.mp3"
    ],
    "Ying Yang Twins": [
        "https://s3.amazonaws.com/rap-adlibs/YingYangTwins_haaan.mp3"
    ],
    "Young Jeezy": [
        "https://s3.amazonaws.com/rap-adlibs/YoungJeezy_aye.mp3",
        "https://s3.amazonaws.com/rap-adlibs/YoungJeezy_haha.mp3",
        "https://s3.amazonaws.com/rap-adlibs/YoungJeezy_yeah.mp3"
    ],
    "Young Thug": [
        "https://s3.amazonaws.com/rap-adlibs/YoungThug_nonsense.mp3",
        "https://s3.amazonaws.com/rap-adlibs/YoungThug_ooh.mp3"
    ],
    "2 Chainz": [
        "https://s3.amazonaws.com/rap-adlibs/2Chainz_2chainz.mp3",
        "https://s3.amazonaws.com/rap-adlibs/2Chainz_tellEm.mp3",
        "https://s3.amazonaws.com/rap-adlibs/2Chainz_true.mp3",
        "https://s3.amazonaws.com/rap-adlibs/2Chainz_yah.mp3"
    ],
    "21 Savage": ["https://s3.amazonaws.com/rap-adlibs/21Savage_21.mp3"],
    "3 6 Mafia": [
        "https://s3.amazonaws.com/rap-adlibs/DJPaul_various.mp3",
        "https://s3.amazonaws.com/rap-adlibs/JuicyJ_various2.mp3"
    ],
    "50 Cent": [
        "https://s3.amazonaws.com/rap-adlibs/50Cent_g-unit.mp3",
        "https://s3.amazonaws.com/rap-adlibs/50Cent_its50.mp3",
        "https://s3.amazonaws.com/rap-adlibs/50Cent_laugh.mp3",
        "https://s3.amazonaws.com/rap-adlibs/50Cent_yeah.mp3"
    ],
}
