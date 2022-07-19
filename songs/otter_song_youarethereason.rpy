init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_youarethereason",
            category=[mas_songs.TYPE_SHORT],
            prompt="You Are the Reason",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_youarethereason:
    m 1eua "{i}~And there goes my mind racing~{/i}"
    m 1dkbsa "{i}~And you are the reason~{/i}"
    m 1dkbsb "{i}~That I'm still breathing~{/i}"
    m 1fkbsa "{i}~I'd climb every mountain~{/i}"
    m 1rkbsa "{i}~And swim every ocean~{/i}"
    m 1ekbsa "{i}~Just to be with you~{/i}"
    m 1dkbsa "{i}~Oh, 'cause I need you to see~{/i}"
    m 1dkbsb "{i}~That you are the reason~{/i}"
    m 1fkbsa "..."
    m 7ekbsa "I would give everything to be with you, [player]."
    m 1ekbsb "You are my reason to everything I do."
    m 1eubsa "I love you so much!"
    return "love"
