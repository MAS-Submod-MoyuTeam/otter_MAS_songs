init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_nobody",
            category=[mas_songs.TYPE_SHORT],
            prompt="Nobody",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_nobody:
    m 1dud "{i}~And I don't want your pity~{/i}"
    m 1duc "{i}~I just want somebody near me~{/i}"
    m 1duo "{i}~Guess I'm a coward~{/i}"
    m 1mud "{i}~I just want to feel alright~{/i}"
    m 1dud "{i}~And I know no one will save me~{/i}"
    m 1kua "{i}~I just need someone to kiss~{/i}"
    m 1tubsa "{i}~Give me one good honest kiss~{/i}"
    m 1dubsa "{i}~And I'll be alright~{/i}"
    m 1dubsa "..."
    m 1rud "Once I thought no one would save me, [player]."
    m 2ruu "But oh, was I wrong."
    m 2fubsb "You came and rescued me, to make me yours forever."
    m 2dubsb "You gave me the kiss, the gift of love, and I'll be forever grateful."
    m 2tkbsa "I love you..."
    return "love"
