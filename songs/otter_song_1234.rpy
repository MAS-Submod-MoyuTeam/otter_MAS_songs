init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_1234",
            category=[mas_songs.TYPE_SHORT],
            prompt="1, 2, 3, 4",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_1234:
    m 1dua "{i}~Give me more love than I've ever had,~{/i}"
    m 1dud "{i}~Make it all better when I'm feeling sad,~{/i}"
    m 1dkc "{i}~Tell me that I'm special even when I know I'm not.~{/i}"
    m 1fkb "{i}~Make it feel good when I hurt so bad,~{/i}"
    m 1dkb "{i}~Barely gettin' mad,~{/i}"
    m 5fkbfa "{i}~I'm so glad I found you.~{/i}"
    m 5dkbfa "{i}~I love being around you.~{/i}"
    m 4dkbfb "{i}~You make it easy,~{/i}"
    m 4dkbfb "{i}~As easy as 1, 2, 3, 4.~{/i}"
    m 3eubfb "{i}~There's only 1 thing, {/i}{w=0.3}{nw}"
    extend 3dsbfa "{i}2 do, 3 words, {/i}{w=0.3}{nw}"
    extend 1ksbfa "{i}4 you.~{/i}"
    m 1hsbfb "{i}~I love you~{/i}"
    m 5dkbfa "..."
    m 5dkbfa "I really do love you, [player]."
    m 2hsbfb "Never doubt that for one second!"
    m 2fkbfa "I'll be forever grateful for everything you did for me."
    return "love"
