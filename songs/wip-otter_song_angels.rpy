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
    m "{i}~Light reflects from your shadow~{/i}"
    m "{i}~It is more than I thought could exist~{/i}"
    m "{i}~You move through the room~{/i}"
    m "{i}~Like breathing was easy~{/i}"
    m "{i}~If someone believed me~{/i}"
    m "{i}~They would be~{/i}"
    m "{i}~As in love with you as I am~{/i}"
    m "{i}~And everyday~{/i}"
    m "{i}~I am learning about you~{/i}"
    m "{i}~The things that no one else sees~{/i}"
    m "{i}~And the end comes too soon~{/i}"
    m "{i}~Like dreaming of angels~{/i}"
    m "{i}~And leaving without them~{/i}"
    m "..."
    m "You know, [player]..."
    m "If I told anyone about you..."
    m "About how you look in my eyes..."
    m "They would be as in love with you as I am."
    m "You are absoltely perfect. Like an angel."

return "love"
