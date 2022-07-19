#better than heaven, by jhana boy, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 10 python:
    def _otterMod_checkConditionals_1():
        if persistent.gender == 'F' and mas_isMoniNormal(higher=True):
            mas_showEVL("otter_song_betterthanheaven", "EVE", random=True)
    store.mas_submod_utils.registerFunction("ch30_minute", _otterMod_checkConditionals_1)

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_betterthanheaven",
            category=[mas_songs.TYPE_SHORT],
            prompt="Better Than Heaven",
        ),
        code="SNG"
    )

label otter_song_betterthanheaven:
    m 1dubfa "{i}~You're my girlfriend~{/i}"
    m 1dubfb "{i}~Dreamed it every night this week~{/i}"
    m 1dubfa "{i}~You're my girlfriend~{/i}"
    m 5fubfa "{i}~We were just lost in video games~{/i}"
    m 5rubfb "{i}~It's better than heaven~{/i}"
    m 5dubfd "{i}~Mopin' all day again~{/i}"
    m 3dubfu "{i}~Your greenish eyes in my head~{/i}"
    m 3dubfo "{i}~All I do is lie in bed~{/i}"
    m 3lubfsdrd "{i}~I may as well just be dead~{/i}"
    m 2dubfu "{i}~I wanna touch her~{/i}"
    m 2dubfu "{i}~I wanna be close with her~{/i}"
    m 2tubfa "{i}~I wanna feel her~{/i}"
    m 2tubfa "{i}~I want to be over her~{/i}"
    m 2gubfa "{i}~And it's better than heaven~{/i}"
    m 2dubfa "..."
    m 2dubfb "You know, [player]..."
    m 5dubfa "When I close my eyes before bed, I always imagine you singing this to me."
    m 5dubfb "Stroking my hair..."
    extend 5fubfa " and looking into my eyes."
    m 5fubfb "I can't wait to cross over and sing this song to you too."
    m 5kubfa "To my beautiful girlfriend."
    m 4dubfa "Being yours is be better than heaven itself."
    m 4hubfb "I love you!"
    return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
