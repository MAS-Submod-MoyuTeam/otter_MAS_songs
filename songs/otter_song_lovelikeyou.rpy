init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_lovelikeyou",
            category=[mas_songs.TYPE_SHORT],
            prompt="Love Like You",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_lovelikeyou:
    m 2dsbsd "{i}~If I could begin to be~{/i}"
    m 2fsbsa "{i}~Half of what you think of me~{/i}"
    m 4dsbsb "{i}~I could do about anything~{/i}"
    m 4lsbsb "{i}~I could even learn how to love~{/i}"
    m 2wsbsa "{i}~When I see the way you act~{/i}"
    m 2rsbsb "{i}~Wondering when I'm coming back~{/i}"
    m 2dsbsb "{i}~I could do about anything~{/i}"
    m 2dsbsb "{i}~I could even learn how to love {/i}"
    extend 2fsbsb "{i}like you~{/i}"
    m 2dsbsd "{i}~I always thought I might be bad~{/i}"
    m 2dsbsd "{i}~Now I’m sure that it's true~{/i}"
    m 2ssbsd "{i}~‘Cause I think you’re so good~{/i}"
    m 2rsbsd "{i}~And I’m nothing like you~{/i}"
    m 5fsbsa "{i}~Look at you go~{/i}"
    m 5hsbsa "{i}~I just adore you~{/i}"
    m 2dsbsd "{i}~I wish that I knew~{/i}"
    m 2rsbsd "{i}~What makes you think I'm so special~{/i}"
    m 4rsbsd "{i}~If I could begin to do~{/i}"
    m 4fsbsu "{i}~Something that does right by you~{/i}"
    m 4dsbsu "{i}~I would do about anything~{/i}"
    m 4dsbsb "{i}~I would even learn how to love~{/i}"
    m 2fsbsb "{i}~When I see the way you look~{/i}"
    m 2dsbsb "{i}~Shaken by how long it took~{/i}"
    m 5dsbsa "{i}~I could do about anything~{/i}"
    m 5dsbfb "{i}~I could even learn how to love like you~{/i}"
    m 5dsbsd "{i}~Love me, like you...~{/i}"
    m 5dsbfa "..."
    m 5fsbfb "I wish I could see myself through your eyes, [player]."
    m 5rsbfu "And I also wish you could see yourself from my point of view."
    m 5rsbsd "If you could love yourself as I love you..."
    m 5dsbfa "..."
    m 5dsbfb "Just know that I learn how to love everyday, with you."
    m 5fsbfa "The best part of me."
    return "love"
