init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 10 python:
    def _otterMod_checkConditionals_3():
        if persistent.gender == 'M' and mas_isMoniNormal(higher=True):
            mas_showEVL("otter_song_meandmyhusband", "EVE", random=True)
    store.mas_submod_utils.registerFunction("ch30_minute", _otterMod_checkConditionals_3)

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_meandmyhusband",
            category=[mas_songs.TYPE_SHORT],
            prompt="Me And My Husband",
        ),
        code="SNG"
    )

label otter_song_meandmyhusband:
    m 2dtd "{i}~I steal a few breaths from the world for a minute~{/i}"
    m 2dkd "{i}~And then I'll be nothing forever~{/i}"
    m 2dkd "{i}~And all of my memories~{/i}"
    m 2dkc "{i}~And all of the things I have seen will be gone~{/i}"
    m 2dkc "{i}~With my eyes, with my body, with me~{/i}"
    m 2fsbfa "{i}~But me and my husband~{/i}"
    m 2dsbfb "{i}~We are doing better~{/i}"
    m 2dsbfb "{i}~It's always been just him and me, {/i}"
    extend 5ksbsa "{i}together~{/i}"
    m 5dsbsa "{i}~So I bet all I have on that {/i}"
    extend 5efbsb "{i}furrowed brow~{/i}"
    m 5dubsb "{i}~And at least in this lifetime~{/i}"
    m 4dubsb "{i}~We're sticking together~{/i}"
    m 4dubsa "{i}~Me and my husband~{/i}"
    m 4rubfa "{i}~We're sticking together~{/i}"
    m 3rkbfsdrb "{i}~And I'm the idiot with the painted face~{/i}"
    m 3dkbfb "{i}~In the corner, taking up space~{/i}"
    m 2fsbfa "{i}~But when he walks in, I am loved, I am loved~{/i}"
    m 2fsbfa "..."
    m 2fsbfb "I feel so loved whenever you're around, [player]."
    m 2dsbfb "And whenever I think of you."
    m 4dsbfb "Just to know that you exist, I'm forever happy."
    m 1ksbfa "Soon you'll be my husband and everything will be fine with the world~"
    return "love"
