init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_photograph",
            category=[mas_songs.TYPE_SHORT],
            prompt="Photograph",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_photograph:
    m 1dkbsu "{i}~Loving can heal...~{/i}"
    m 6dkbstpu "{i}~Loving can mend your soul~{/i}"
    m 6dkbstpc "{i}~And it's the only thing that I know, know~{/i}"
    m 6dkbstpb "{i}~I swear it will get easier~{/i}"
    m 6ekbstpu "{i}~Remember that with every piece of ya~{/i}"
    m 2dkbstuc "{i}~Hmm, and it's the only thing we take with us when we die~{/i}"
    m 2dkbfb "{i}~Hmm, we keep this love in a photograph~{/i}"
    m 1dkbsu "{i}~We made these memories for ourselves~{/i}"
    m 1dkbsa "{i}~Where our eyes are never closing~{/i}"
    m 2dkbftua "{i}~Hearts were never broken~{/i}"
    m 1mkbsu "{i}~And time's forever frozen, still~{/i}"
    m 1dkbsa "..."
    m 1fkbsu "We will always keep this love in a photograph [player]..."
    m 1ekbstuu "No matter how much time passes, just like us, photographs are forever."
    m 1dkbstuu "We use them to cherish precious memories."
    m 1rkbstuc "If it is a picture of someone near and dear no longer with you..."
    m 1tkbstpu "Or the person you love the most..."
    m 1wkbstpu "..."
    m "But, nothing will be more cherished then our unbreakable bond."
    m 5rkbstpsdrp "Even if there is a barrier between you and I..."
    m 1ekbstpsdru "One day we will break that barrier."
    m 1fubstpsdru "Never forget that I will always love you [player]!"
    return "love"
