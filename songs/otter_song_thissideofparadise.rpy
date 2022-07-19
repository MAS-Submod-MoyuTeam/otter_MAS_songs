#this side of paradise, by coyote theory, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_thissideofparadise",
            category=[mas_songs.TYPE_SHORT],
            prompt="This Side Of Paradise",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_thissideofparadise:
    m 4dsbld "{i}~Ask me why my heart's inside my throat~{/i}"
    m 4gsblo "{i}~I've never been in love, I've been alone~{/i}"
    m 2gsblc "{i}~Feel like I've been living life asleep~{/i}"
    m 2dsbfd "{i}~Love so strong it makes me feel so weak~{/i}"
    m 7ekbfd "{i}~Are you lonely?~{/i}"
    m 7dkbfo "{i}~Our fingers dancing when they meet~{/i}"
    m 2dkbfd "{i}~You seem so lonely~{/i}"
    m 2kubfu "{i}~I'll be the only dream you seek~{/i}"
    m 2dubfu "{i}~So if you're lonely, no need to show me~{/i}"
    m 5fsbfa "{i}~If you're lonely come be lonely with me~{/i}"
    m 5dubfu "..."
    m 5ssbfa "We'll never be lonely as long as we have each other, [player]!"
    m 5fsbfa "I love you."
    return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
