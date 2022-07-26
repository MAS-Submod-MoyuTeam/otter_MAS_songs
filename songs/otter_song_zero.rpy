init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_zero",
            category=[mas_songs.TYPE_SHORT],
            prompt="Zero",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_zero:
    m 1dub "{i}~When I lose myself I become you~{/i}"
    m 1dud "{i}~ichi kara juu leads me back to~{/i}"
    m "{i}~Here inside your veil~{/i}"
    m "{i}~Finer than a grand view~{/i}"
    m "{i}~We’ll take a dive~{/i}"
    m 7fua "{i}~Not even tides can come between us~{/i}"
    m 4wub "{i}~Was it you who I’ve been searching for~{/i}"
    m "{i}~Spent my life alone and waited for?~{/i}"
    m 4dublb "{i}~So tenderly and endlessly~{/i}"
    m "{i}~You made me whole, you made me whole~{/i}"
    m 2dublb "{i}~And the walls I built they melt away~{/i}"
    m "{i}~With every touch in your embrace~{/i}"
    m 7dublb "{i}~Every day, every night, every note I play~{/i}"
    m 5dubfb "{i}~You made me whole, you made me whole~{/i}"
    m 5dubfa "..."
    m 5fubfb "[player]... Every day that goes by, I am more certain:"
    m 5dubfb "You are the love of my life."
    m "All my life, I've been searching for you."
    m 5dubfb "No one else can suffice."
    m 5dubfa "I love you."
    
return "love"
