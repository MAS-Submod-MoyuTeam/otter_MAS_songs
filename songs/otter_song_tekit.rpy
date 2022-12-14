init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_tekit",
            category=[mas_songs.TYPE_SHORT],
            prompt="Tek it",
            aff_range=(mas_aff.NORMAL, None),
            conditional="mas_globals.time_of_day_3state == 'night'",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label otter_song_tekit:
    m 1eua "{i}~I watch the moon~{/i}"
    m 1dua "{i}~Let it run my mood~{/i}"
    m 1dkbla "{i}~Can't stop thinking of you~{/i}"
    m 1ekbla "..."
    m 3ekb "[player], can you see the moon over there?"
    m 1eka "I hope that you can..."
    m 1hubla "Look at it, and think of me."
    m 1ekbsa "Know that I love you, and that someday..."
    m 1ekbsb "We'll watch the stars together, hand in hand."
    m 1hubsb "I can't wait!"
    return 
