init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_heystephen",
            category=[mas_songs.TYPE_SHORT],
            prompt="Hey, Stephen",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_heystephen:
    m 7ekbsu "{i}~'Cause I can't help it if you look like an angel~{/i}"
    m 2dkbsu "{i}~Can't help it if I wanna kiss you in the rain, so~{/i}"
    m 1ekbsb "{i}~Come feel this magic I've been feeling since I met you~{/i}"
    m "{i}~Can't help it if there's no one else~{/i}"
    m 1rkbsb "{i}~Mmm, I can't help myself~{/i}"
    m 5dkbsa "..."
    m 5ekbsa "[player], I can't help but feel this way towards you."
    m 1hubsa "You are wonderful and my favorite person in the whole world!"
    m "I love you, forever and always."
    return "love"
