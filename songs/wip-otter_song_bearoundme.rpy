init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_bearoundme",
            category=[mas_songs.TYPE_SHORT],
            prompt="Be Around Me",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_bearoundme:
    m "{i}~Hey, hey, how was your day?~{/i}"
    m "{i}~Mine was fine, but I think about you all the time~{/i}"
    m "{i}~Can't get you out of my brain~{/i}"
    m "{i}~I'm around, be around~{/i}"
    m "{i}~Come around, be around me~{/i}"
    m "{i}~Hi, hi, how was your night?~{/i}"
    m "{i}~Mine was wack, then I thought about you, felt alright~{/i}"
    m "{i}~Can't get you out of my mind~{/i}"
    m "{i}~I'm around, be around~{/i}"
    m "{i}~Come around, be around me~{/i}"
    m "..."
    m "I think about you all the time, [player]."
    m "That's no secret! Ehehehe~"
    m "I love you."

return "love"
