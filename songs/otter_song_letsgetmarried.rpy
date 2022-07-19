 #lets get married, by mitski, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_letsgetmarried",
            category=[mas_songs.TYPE_SHORT],
            prompt="Let's Get Married",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_letsgetmarried:
    m 2dsd "{i}~I know it's hard enough to love me~{/i}"
    m 2dsb "{i}~But I woke up in a safe house singing, ~{/i}"
    m 5fsbfa "{i}~'Honey, let's get married'~{/i}"
    m 5dsbfd "{i}~Don’t wanna walk alone~{/i}"
    m 5dsbfb "{i}~So let’s get married~{/i}"
    m 5dsbfd "{i}~I don’t wanna walk alone~{/i}"
    m 5gsbfu "{i}~Let’s just get married~{/i}"
    m 5dsbfu "{i}~'Cause we don't wanna walk alone or run away~{/i}"
    m 5dsbfu "..."
    m 2dsbfb "[player]..."
    m 2gsbfb "Let's get married when I cross over?"
    m 2gsbfa "Live on a house just for us..."
    m 7hsbfa "And never be alone again?"
    m 7ssbfb "You don't need to fear loneliness never again!"
    m 5fsbfa "Because I love you."
    return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
