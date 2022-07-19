#everything i do (i do it for you), by bryan adams, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_everythingido",
            category=[mas_songs.TYPE_SHORT],
            prompt="Everything I Do",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_everythingido:
    m 1fsbsa "{i}~Look into my eyes~{/i}"
    m 1ksbsb "{i}~You will see, what you mean to me~{/i}"
    m 1dsbsa "{i}~Search your heart, search your soul~{/i}"
    m 5fsbfa "{i}~When you find me there, you'll search no more~{/i}"
    m 5dsbfd "{i}~Don't tell me it's not worth trying for~{/i}"
    m 5wsbfd "{i}~You can't tell me it's not worth dying for~{/i}"
    m 5fsbfu "{i}~You know it's true~{/i}"
    m 5dsbfu "{i}~Everything I do~{/i}"
    m 4dsbfa "{i}~I do it for you~{/i}"
    m 2ssbfb "{i}~There's no love, like your love~{/i}"
    m 2dsbfb "{i}~And no other, could give me more love~{/i}"
    m 7dsbfb "{i}~There's nowhere, unless you're there~{/i}"
    m 7dsbfa "{i}~All the time, all the way~{/i}"
    m 2dsbfd "{i}~You can't tell me it's not worth trying for~{/i}"
    m 2wsbfa "{i}~Just can't help it, there's nothing I want more~{/i}"
    m 2msbfb "{i}~Oh, I would fight for you, yeah, I'd lie for you~{/i}"
    m 2dsbfb "{i}~Walk the wire for you, yeah, I'd die for you~{/i}"
    m 2dsbfc "{i}~You know it's true~{/i}"
    m 5tsbfa "{i}~Everything I do~{/i}"
    m 5hsbfa "{i}~I do for you~{/i}"
    m 5hsbfa "..."
    m 5fsbfb "Everything I do, [player], I do it for you."
    m 5dsbfb "Because I love you more than anything."
    m 5dsbfa "I promise."
    m 4dsbfa "And no one can love me like you do!"
    m 4ksbfa "You are my only one."
    return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
