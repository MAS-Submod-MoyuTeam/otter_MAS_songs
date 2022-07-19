init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 10 python:
    def _otterMod_checkConditionals_2():
        if persistent.gender == 'F' and mas_isMoniNormal(higher=True):
            mas_showEVL("otter_song_2step", "EVE", random=True)
    store.mas_submod_utils.registerFunction("ch30_minute", _otterMod_checkConditionals_2)

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_2step",
            category=[mas_songs.TYPE_SHORT],
            prompt="2 Step",
        ),
        code="SNG"
    )

label otter_song_2step:
    m 1dud "{i}~I had a bad week~{/i}"
    m 1duc "{i}~Spent the evening pretending it wasn't that deep~{/i}"
    m 1ekd "{i}~You could see in my eyes that it was taking over~{/i}"
    m 1dkc "{i}~I guess I was just blind and caught up in the moment~{/i}"
    m 1dkb "{i}~You know you take all of my stress right down~{/i}"
    m 4dkblb "{i}~Help me get it off my chest and out~{/i}"
    m 5fkbfa "{i}~I think maybe you and me~{/i}"
    m 5dkbfa "{i}~Oh, we should head out to the place where the music plays~{/i}"
    m 4dkbfb "{i}~And then, "
    extend "{i}we'll go all night~{/i}"
    m 1dubfa "{i}~Two-stepping with the woman I love~{/i}"
    m 1subfa "{i}~All my troubles turn to nothing when I'm in your eyes, electrified~{/i}"
    m 1fubfb "{i}~We'll keep turning up and go all night~{/i}"
    m 1dublb "{i}~Oh, we had dips and falls in our time~{/i}"
    m 1lubld "{i}~But we know what it feels to be low, then up, alone and loved~{/i}"
    m 1hubfu "{i}~And all we need is us to go all~{/i}"
    m 1lubfu "..."
    m 1eubfb "Thank you for making all my stress go away, [player]."
    m 1hubfb "You're the best girlfriend I could ask for!"
    m 1kubfa "I want to spend eternity with you, dancing and having fun."
    m 5fubfa "I love you..."

    return "love"
