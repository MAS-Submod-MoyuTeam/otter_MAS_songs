init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_comehere",
            category=[mas_songs.TYPE_SHORT],
            prompt="Come Here",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_comehere:
    m "{i}~No I'm not impossible to touch~{/i}"
    m "{i}~I have never wanted you so much~{/i}"
    m "{i}~Come here, come here~{/i}"
    m "{i}~Have I never laid down by your side~{/i}"
    m "{i}~Baby, let's forget about this pride~{/i}"
    m "{i}~Come here, come here~{/i}"
    m "..."
    m "You know, [mas_get_player_nickname()], there is no pride when the topic is you and I."
    m "I can't wait to finally touch you."
    m "To gently whisper in your ear, 'come here'..."
    m "I love you..."
    
return "love"
