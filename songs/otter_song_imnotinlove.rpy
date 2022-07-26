init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_imnotinlove",
            category=[mas_songs.TYPE_SHORT],
            prompt="I'm Not In Love",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_imnotinlove:
    m 2dkd "{i}~I'm not in love~{/i}"
    m 2ekd "{i}~So don't forget it~{/i}"
    m 1rkc "{i}~It's just a silly phase I'm going through~{/i}"
    m 1dud "{i}~And just because I call you up~{/i}"
    m "{i}~Don't get me wrong~{/i}"
    m "{i}~Don't think you've gotten me~{/i}"
    m 1dkbld "{i}~I'm not in love~{/i}"
    m 1rkblc "{i}~No, no~{/i}"
    m 5dkbsa "..."
    m 3hkbsb "It's obvious to everyone that I am so in love with you, [player]."
    m 3hubsb "I could never be able to hide it!"
    m 3hubsu "Ehehehe~"
    return "love"
