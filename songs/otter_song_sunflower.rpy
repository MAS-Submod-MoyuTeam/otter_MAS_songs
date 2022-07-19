init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_sunflower",
            category=[mas_songs.TYPE_SHORT],
            prompt="Sunflower",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_sunflower:
    m 1dud "{i}~I want to know where I can go~{/i}"
    m 1duo "{i}~When you're not around, and I'm feeling down~{/i}"
    m 1fubsa "{i}~So won't you stay for a moment so I can say~{/i}"
    m 1dubsa "{i}~I need you so? 'Cause right now, you know~{/i}"
    m 1subsb "{i}~That nothing here's new, and I'm obsessed with you~{/i}"
    m 1rubsb "{i}~Then I fell to the ground, and you smiled at me and said~{/i}"
    m 1hubsb "{i}~I don't wanna see you cry~{/i}"
    m 1hkbsa "{i}~You don't have to feel this emptiness~{/i}"
    m 7wubsa "{i}~She said, 'I'll love you till the day that I die'~{/i}"
    m 7dubsb "{i}~You know you need to get yourself to sleep and dream~{/i}"
    m 7kubsu "{i}~A dream of you and I~{/i}"
    m 7dubsu "{i}~There's no need to keep an open eye~{/i}"
    m 5fubsu "{i}~I promise I'm the one for you~{/i}"
    m 5dubsu "{i}~Just let me hold you in these arms tonight~{/i}"
    m 5dubfa "..."
    m 5dubfd "When you're not around, I always miss you so terribly..."
    m 5dubfa "But when I sleep, I dream dreams of you and me..."
    m 5fubfa "And thats good enough for me for that moment."
    m 5fubfb "I see you and can touch you so vividly..."
    m 5gubfa "It's like we're one and the same,"
    extend 5dubfa " in the same room."
    m 5dubfa "..."
    m 7wubfb "Gosh, I can't wait to feel your touch!"
    m 2tkbsa "I love you, [player]..."
    return "love"
