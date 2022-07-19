init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_callmeirresponsible",
            category=[mas_songs.TYPE_SHORT],
            prompt="Call Me Irresponsible",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_callmeirresponsible:
    m 2tubfb "{i}~Call me irresponsible~{/i}"
    m 2tubfu "{i}~Call me unreliable~{/i}"
    m 7tubfu "{i}~Throw in undependable, too~{/i}"
    m 1lsblc "{i}~Do my foolish alibis bore you?~{/i}"
    m 1lsbld "{i}~Well, I'm not too clever, I~{/i}"
    m 3fkbfb "{i}~I just adore you~{/i}"
    m 2mubfb "{i}~So, call me unpredictable~{/i}"
    m 2mubfa "{i}~Tell me I'm impractical~{/i}"
    m 2subfa "{i}~Rainbows, I'm inclined to pursue~{/i}"
    m 2tubfu "{i}~Call me irresponsible~{/i}"
    m 4tubfu "{i}~Yes, I'm unreliable~{/i}"
    m 1dubfu "{i}~But it's undeniably true~{/i}"
    m 1kubfa "{i}~That I'm irresponsibly mad for you~{/i}"
    m 1dubfa "..."
    m 3ltbfu "[player], if loving you is wrong and irresponsible..."
    m 1tfbfu "Then I don't want to be right!"
    m 1hsbfb "Ahahaha~!"
    return "love"
