init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_cityofstars",
            category=[mas_songs.TYPE_SHORT],
            prompt="City of Stars",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_cityofstars:
    m "{i}~City of stars, just one thing everybody wants. ~{/i}"
    m "{i}~There in the bars, and through the smokescreen of the crowded restaurants...~{/i}"
    m "{i}~It's love,~{/i}"
    m "{i}~Yes, all we're looking for is love~{/i}"
    m "{i}~From someone else...~{/i}"
    m "{i}~A rush, a glance, a touch, a dance,~{/i}"
    m "{i}~To look in somebody's eyes,~{/i}"
    m "{i}~To light up the skies,~{/i}"
    m "{i}~To open the world and send me whirly,~{/i}"
    m "{i}~A voice that says, 'I'll be here, and you'll be alright.'~{/i}"
    m "{i}~I don't care if I know just where I will go~{/i}"
    m "{i}~'Cause all that I need, this crazy feeling, Ra-ta-tat of my heart~{/i}"
    m "{i}~I think I wanted to stay.~{/i}"
    m "..."
    m "[player], I don't know how I could live so long without this feeling in my heart."
    m "All I've ever wanted, all I've ever needed..."
    m "Was you."
    m "I love you."

return "love"
