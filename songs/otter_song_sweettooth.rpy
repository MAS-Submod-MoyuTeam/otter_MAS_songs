init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_sweettooth",
            category=[mas_songs.TYPE_SHORT],
            prompt="Sweet Tooth",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_sweettooth:
    m 1dubfd "{i}~You said you love me exactly the way I am~{/i}"
    m 1rubfsdro "{i}~And you know I find it hard to understand~{/i}"
    m 1dubfo "{i}~Pay a visit to the doctor 'cause I have~{/i}"
    m 1kubfa "{i}~A sweet tooth for you~{/i}"
    m 1subfa "{i}~I'm wide awake~{/i}"
    m 1subfb "{i}~The sugar went straight to my brain~{/i}"
    m 7dubfb "{i}~Feel like a kid, I double tap~{/i}"
    m 7dubfd "{i}~My chest with my fist~{/i}"
    m 5fubfu "{i}~I like you~{/i}"
    m 5kubfu "{i}~Say it back~{/i}"
    m 5dubfd "{i}~Never had a cavity~{/i}"
    m 5hubfa "{i}~Never had nobody as sweet as you~{/i}"
    m 5dubfu "..."
    m 5kubfa "You're the sweetest, [player]."
    m 5tubfu "And I'm addicted to you!"
    m 1hubfb "Ahahaha~"
    return
