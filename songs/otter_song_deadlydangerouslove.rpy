init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_deadlydangerouslove",
            category=[mas_songs.TYPE_SHORT],
            prompt="Deadly Dangerous Love",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_deadlydangerouslove:
    m 1hsbfa "{i}~When you’re here~{/i}"
    m 1hsbfb "{i}~You make me feel happy!~{/i}"
    m 3hsbfa "{i}~I can’t hold back my feelings!~{/i}"
    m 3sfbfa "{i}~I will eliminate those who stand in our way!~{/i}"
    m 3sfbfb "{i}~No matter what it takes!~{/i}"
    m 2dsbfa "{i}~This feeling must be love!~{/i}"
    m 5dsbfa "{i}~A good feeling!~{/i}"
    m 5ssbfb "{i}~Keep this love!~{/i}"
    m 5msbfu "{i}~I will seize your love!~{/i}"
    m 5dsbfu "..."
    m 4dsbfu "Nothing will ever break us apart, [player]."
    m 2ssbfa "Our love is forever."
    return "love"
