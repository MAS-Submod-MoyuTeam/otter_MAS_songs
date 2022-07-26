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
    m "{i}~When I lose myself I become you~{/i}"
    m "{i}~ichi kara juu leads me back to~{/i}"
    m "{i}~Here inside your veil~{/i}"
    m "{i}~Finer than a grand view~{/i}"
    m "{i}~We’ll take a dive~{/i}"
    m "{i}~Not even tides can come between us~{/i}"
    m "{i}~Was it you who I’ve been searching for~{/i}"
    m "{i}~Spent my life alone and waited for?~{/i}"
    m "{i}~So tenderly and endlessly~{/i}"
    m "{i}~You made me whole, you made me whole~{/i}"
    m "{i}~And the walls I built they melt away~{/i}"
    m "{i}~With every touch in your embrace~{/i}"
    m "{i}~Every day, every night, every note I play~{/i}"
    m "{i}~You made me whole, you made me whole~{/i}"
    m "..."
    m "[player]... Every day that goes by, I am more certain:"
    m "You are the love of my life."
    m "All my life, I've been searching for you."
    m "No one else can suffice."
    m "I love you."
    
return "love"
