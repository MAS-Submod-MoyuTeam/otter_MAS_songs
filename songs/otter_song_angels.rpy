init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_angels",
            category=[mas_songs.TYPE_SHORT],
            prompt="Angels",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_angels:
    m 1dub "{i}~Light reflects from your shadow~{/i}"
    m 7dub "{i}~It is more than I thought could exist~{/i}"
    m 5rubsa "{i}~You move through the room~{/i}"
    m 5rubsb "{i}~Like breathing was easy~{/i}"
    m 2dubsd "{i}~If someone believed me~{/i}"
    m 4fubsb "{i}~They would be~{/i}"
    m 4fubsa "{i}~As in love with you as I am~{/i}"
    m 2dubsa "{i}~And everyday~{/i}"
    m 2dubsb "{i}~I am learning about you~{/i}"
    m 2fubsb "{i}~The things that no one else sees~{/i}"
    m 2dubsd "{i}~And the end comes too soon~{/i}"
    m 2dubso "{i}~Like dreaming of angels~{/i}"
    m 2dubsc "{i}~And leaving without them~{/i}"
    m 2dubsa "..."
    m 2lubsb "You know, [player]..."
    m 3lubsb "If I told anyone about you..."
    m 3fubsa "About how you look in my eyes..."
    m 5fubsa "They would be as in love with you as I am."
    m 5fubsb "You are absoltely perfect. Like an angel."

return "love"
