init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_teeshirt",
            category=[mas_songs.TYPE_SHORT],
            prompt="Tee Shirt",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_teeshirt:
    m 1dub "{i}~In the morning when you wake up~{/i}"
    m 1dkbla "{i}~I like to believe you are thinking of me~{/i}"
    m 1dub "{i}~And when the sun comes through your window~{/i}"
    m 3ekbsa "{i}~I like to believe you've been dreaming of me~{/i}"
    m 1dka "{i}~I know~{/i}"
    m 1eka "{i}~'Cause I'd spend half this morning~{/i}"
    m 1ekblb "{i}~Thinking about the t-shirt you sleep in~{/i}"
    m 1ekbla "..."
    m 1ekbsa "[player], you're my first thought as soon as I wake up."
    m "And my last thought when I go to bed."
    m 1dkbsb "I've never felt this before..."
    m 3hkbsb "I'm so in love, my chest hurts."
    m 3hubsb "But don't worry about me!"
    m 3tubsa "It's the best pain I've ever felt."
    m 3ekbsb "I love you..."
    return "love"
