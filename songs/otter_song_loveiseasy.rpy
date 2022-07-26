init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_loveiseasy",
            category=[mas_songs.TYPE_SHORT],
            prompt="Love is easy",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_loveiseasy:
    m 1eub "{i}~Today I'm laughing the clouds away~{/i}"
    m 1lua "{i}~I hear what the flowers say~{/i}"
    m 3eua "{i}~Drinking a drop of rain~{/i}"
    m 1ekb "{i}~And I see the places that I have been~{/i}"
    m 1eub "{i}~A place that I've never seen~{/i}"
    m 1hua "{i}~My side of the grass is green~{/i}"
    m 1hub "{i}~Oh I can't believe that it's so simple~{/i}"
    m 1dub "{i}~It feels so natural to me~{/i}"
    m 7dubsa "{i}~If this is love, then love is easy~{/i}"
    m 7dkbsa "{i}~It's the easiest thing to do~{/i}"
    m 5dubsb "{i}~If this is love, then love completes me~{/i}"
    m 5dkbsb "{i}~Cause it feels like I've been missing you~{/i}"
    m 1dubsa "{i}~A simple equation~{/i}"
    m 1eubsa "{i}~With no complications to leave you confused~{/i}"
    m 1dkbsa "..."
    m 1ekbsa "Being with love with you is so easy, [player]."
    m 1rubsb "This love makes me feel comfortable, safe, and..."
    extend 3hubsb " the happiest I've ever been."
    m 3hubsa "Thank you for making me feel this way!"
    return "love"
