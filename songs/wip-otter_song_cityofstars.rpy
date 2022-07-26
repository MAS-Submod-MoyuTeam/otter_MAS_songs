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
    m 2dubld "{i}~City of stars, just one thing everybody wants. ~{/i}"
    m "{i}~There in the bars, and through the smokescreen of the crowded restaurants...~{/i}"
    m 7fubla "{i}~It's love,~{/i}"
    m 5fublb "{i}~Yes, all we're looking for is love~{/i}"
    m 5rublb "{i}~From someone else...~{/i}"
    m 5dublb "{i}~A rush, a glance, a touch, a dance,~{/i}"
    m 5tublu "{i}~To look in somebody's eyes,~{/i}"
    m 4sublu "{i}~To light up the skies,~{/i}"
    m "{i}~To open the world and send me whirly,~{/i}"
    m 2dublb "{i}~A voice that says, 'I'll be here, and you'll be alright.'~{/i}"
    m 3dublb "{i}~I don't care if I know just where I will go~{/i}"
    m 2wublb "{i}~'Cause all that I need, this crazy feeling, Ra-ta-tat of my heart~{/i}"
    m 5fubsa "{i}~I think I wanted to stay.~{/i}"
    m 5dubsa "..."
    m 5dubsb "[player], I don't know how I could live so long without this feeling in my heart."
    m "All I've ever wanted, all I've ever needed..."
    m 5fubsb "Was you."
    m 5fubsa "I love you."

return "love"
