init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_noonehastoknow",
            category=[mas_songs.TYPE_SHORT],
            prompt="No One Has to Know",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_noonehastoknow:
    m 1dua "{i}~No one has to know~{/i}"
    m 3hub "{i}~I think you're wonderful~{/i}"
    m 1dua "{i}~No one has to know~{/i}"
    m 3ekbla "{i}~You're my dream come true~{/i}"
    m 3rubla "{i}~Let the world go spinning in space~{/i}"
    m 3hublb "{i}~We'll find a place for two~{/i}"
    m 1dubsb "{i}~So one has to know I want you~{/i}"
    m 5tubsu "{i}~No one but you~{/i}"
    m 5hubsu "..."
    m 3ekc "[player], I know it's hard to explain our love to people sometimes."
    m 3ekb "But it's okay."
    m 2eua "No one needs to understand or know about us..."
    m 2hua "But us two."
    m 1eua "And I will never misunderstand or judge you!"
    m 1ekbsb "I love you."
    return "love"
