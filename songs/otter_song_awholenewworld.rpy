init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_awholenewworld",
            category=[mas_songs.TYPE_SHORT],
            prompt="A Whole New World",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_awholenewworld:
    m 1dublo "{i}~A whole new world~{/i}"
    m 1dublb "{i}~A dazzling place I never knew~{/i}"
    m 7subla "{i}~But when I'm away up here~{/i}"
    m 7subla "{i}~It's crystal clear~{/i}"
    m 1sublb "{i}~That now I'm in a whole new world with you~{/i}"
    m 1dublb "{i}~Unbelievable sights~{/i}"
    m 1hubla "{i}~Indescribable feeling~{/i}"
    m 1dublo "{i}~Soaring, tumbling, freewheeling~{/i}"
    m 1dubld "{i}~Through an endless diamond sky~{/i}"
    m 1sublb "{i}~A whole new world~{/i}"
    m 1sublb "{i}~A hundred thousand things to see~{/i}"
    m 3subla "{i}~I'm like a shooting star~{/i}"
    m 3dubla "{i}~I've come so far~{/i}"
    m 2lubld "{i}~I can't go back to where I used to be~{/i}"
    m 2dublo "{i}~A whole new world~{/i}"
    m 2dubld "{i}~With new horizons to pursue~{/i}"
    m 2hublb "{i}~I'll chase them anywhere~{/i}"
    m 4hublb "{i}~There's time to spare~{/i}"
    m 5fubfa "{i}~Let me share this whole new world with you~{/i}"
    m 5dubfb "{i}~A whole new world~{/i}"
    m 5dubfa "{i}~That's where we'll be~{/i}"
    m 5rubfb "{i}~A thrilling chase~{/i}"
    m 4rubfb "{i}~A wondrous place~{/i}"
    m 1tubfa "{i}~For you and me~{/i}"
    m 1mubfa "..."
    m 1dubfb "When I cross over... Everything will be so new to me, [player]."
    m 1subfu "I can't wait to discover a whole new world with you!"
    m 5dubfb "I love you~"
    return "love"
