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
    m 7fua "{i}~Hey, hey, how was your day?~{/i}"
    m 7lub "{i}~Mine was fine, but I think about you all the time~{/i}"
    m 7hub "{i}~Can't get you out of my brain~{/i}"
    m 2dublb "{i}~I'm around, be around~{/i}"
    m "{i}~Come around, be around me~{/i}"
    m 7dublb "{i}~Hi, hi, how was your night?~{/i}"
    m 7wublo "{i}~Mine was wack, then I thought about you, felt alright~{/i}"
    m 2kublu "{i}~Can't get you out of my mind~{/i}"
    m 5dubsb "{i}~I'm around, be around~{/i}"
    m "{i}~Come around, be around me~{/i}"
    m 5dubsa "..."
    m 5fubsb "I think about you all the time, [player]."
    m 7kubsa "That's no secret! Ehehehe~"
    m 2fubsa "I love you."

return "love"
