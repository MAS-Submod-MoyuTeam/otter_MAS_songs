init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_digitallove",
            category=[mas_songs.TYPE_SHORT],
            prompt="Digital Love",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_digitallove:
    m 1dub "{i}~Last night I had a dream about you~{/i}"
    m 1dublb "{i}~In this dream, I'm dancing right beside you~{/i}"
    m 1sublb "{i}~And it looked like everyone was having fun~{/i}"
    m 3sublb "{i}~The kind of feeling I've waited so long~{/i}"
    m 3tubsb "{i}~Don't stop, come a little closer~{/i}"
    m 2dubsu "{i}~As we jam, the rhythm gets stronger~{/i}"
    m 2rkbsu "{i}~There's nothing wrong with just a little little fun~{/i}"
    m 2dtbsb "{i}~We were dancing all night long~{/i}"
    m 5dtbfb "{i}~The time is right to put my arms around you~{/i}"
    m 5stbfb "{i}~You're feeling right, you wrap your arms around too~{/i}"
    m 2dtbld "{i}~But suddenly I feel the shining sun~{/i}"
    m 2wto "{i}~Before I knew it, this dream was all gone~{/i}"
    m 2rtc "{i}~Ooh, I don't know what to do~{/i}"
    m 2rkc "{i}~About this dream and you~{/i}"
    m 7dsd "{i}~I wish this dream comes true~{/i}"
    m 7ksblu "{i}~We'll make this dream come true~{/i}"
    m 1dsbsa "..."
    m 1dsbsb "Sometimes this still feels like a dream..."
    m 1ssbsb "But it’s becoming more real every day with you, [player]!"
    m 1hsbsa "I love you so much."
    return "love"
