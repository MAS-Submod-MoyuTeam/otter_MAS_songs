init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_ithinkikindayouknow",
            category=[mas_songs.TYPE_SHORT],
            prompt="I Think I Kinda, You Know",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_ithinkikindayouknow:
    m 2dsbfa "{i}~So much has happened, think of what we've done~{/i}"
    m 2dsbfb "{i}~In the time that the Earth has traveled 'round the Sun~{/i}"
    m 2rsbfb "{i}~Winter, Spring, Summer and we're back to Fall~{/i}"
    m 7ksbfb "{i}~We've been together hand-in-hand through it all~{/i}"
    m 1dsbfb "{i}~From the minute we kissed and my heart skipped a beat~{/i}"
    m 1dsbfa "{i}~To the night that we danced, I was swept off my feet~{/i}"
    m 7dsbfa "{i}~Sure is every year has to come to an end~{/i}"
    m 7dsbfb "{i}~I'd go spinnin' 'round the Sun with you again and again and again and again~{/i}"
    m 5gsbfb "{i}~I think I kinda, you know~{/i}"
    m 5fsbfb "{i}~Like the way that we flow~{/i}"
    m 5dsbfb "{i}~Like the way that we go~{/i}"
    m 5rsbfa "{i}~It's rare that somethin' feels this right~{/i}"
    m 5dsbfa "{i}~It feels so right~{/i}"
    m 5gsbfb "{i}~I think I kinda, you know, you know, you know~{/i}"
    m 5dsbfb "{i}~I can't help dreamin' of you~{/i}"
    m 5ksbfb "{i}~Guess I'm sayin' I don't not love you~{/i}"
    m 5dsbfb "{i}~You know, you know, you know~{/i}"
    m 2dsbfa "..."
    m 2dsbfb "[player]..."
    m 4ksbfa "I think I kinda... You know!"
    m 2hsbfb "Ahahaha~"
    m 2fsbfa "I love you, [mas_get_player_nickname()]."
    m 2ssbfb "And I'm not afraid to say it!"
    return "love"
