init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_lastnightonearth",
            category=[mas_songs.TYPE_SHORT],
            prompt="Last Night on Earth",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_lastnightonearth:
    m 1dud "{i}~I text a postcard sent to you~{/i}"
    m 1eka "{i}~Did it go through?~{/i}"
    m 3hubsa "{i}~Sending all my love to you~{/i}"
    m 3hubsb "{i}~You are the moonlight of my life~{/i}"
    m 1dubsb "{i}~Every night~{/i}"
    m "{i}~Giving all my love to you~{/i}"
    m 1dkbsa "{i}~My beating heart belongs to you~{/i}"
    m 1ekbsa "{i}~I walked for miles 'til I found you~{/i}"
    m 1euc "{i}~I'm here to honor you~{/i}"
    m 1ekc "{i}~If I lose everything in the fire~{/i}"
    m 1ekbsa "{i}~I'm sending all my love to you~{/i}"
    m 1dkbsa "..."
    m 1dkbsd "[player], if I lost everything but you..."
    m 1fkbsa "Then I would have lost nothing."
    m 3hubla "I love you..."
    return "love"
