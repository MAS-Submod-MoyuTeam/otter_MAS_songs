init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_makeyoumine",
            category=[mas_songs.TYPE_SHORT],
            prompt="Make You Mine",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_makeyoumine:
    m 5dsbsa "{i}~Well, I will call you darlin' and everything will be okay~{/i}"
    m 5ksbsa "{i}~'Cause I know that I am yours and you are mine~{/i}"
    m 5dsbsd "{i}~Doesn't matter anyway~{/i}"
    m 5gsbsu "{i}~In the night, we'll take a walk, it's nothin' funny~{/i}"
    m 5dsbsu "{i}~Just to talk~{/i}"
    m 4dsbsb "{i}~Put your hand in mine~{/i}"
    m 4fsbsb "{i}~You know that I want to be with you all the time~{/i}"
    m 4hsbsb "{i}~You know that I won't stop until I make you mine~{/i}"
    m 2hsbsa "..."
    m 2gsbsa "I'm so glad you are mine, [player]."
    m 7gsbsb "It means the world to me."
    m 7ssbsb "If you're with me, I feel like we can overcome anything!"
    m 7hsbsb "And I'm always with you too!"
    m 5ksbsa "I'm yours, head to toe."
    m 5hsbsb "Ehehehe~!"
    return
