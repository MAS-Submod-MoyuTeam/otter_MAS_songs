#someone you like, by the girl and the dreamcatcher, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["mas_song_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_someoneyoulike",
            category=[mas_songs.TYPE_SHORT],
            prompt="Someone You Like",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_someoneyoulike:
    m 2dubsu "{i}~I saw you~{/i}"
    m 2tubsu "{i}~With that ribbon in your hair~{/i}"
    m 2tubsb "{i}~Think that I began to stare~{/i}"
    m 2mubsb "{i}~Maybe I'll love you for a while~{/i}"
    m 2dubsd "{i}~A stranger at a table in a place~{/i}"
    m 2kubsa "{i}~And a really pretty face~{/i}"
    m 7rubsa "{i}~I wonder what happens when you smile~{/i}"
    m 7dubsd "{i}~I might never be your hero~{/i}"
    m 1dubsd "{i}~Never been one to fight~{/i}"
    m 1wubsd "{i}~That don't mean that I can't be your Valentine~{/i}"
    m 1rubsd "{i}~I won't be your savior either~{/i}"
    m 1dkbsc "{i}~Couldn't even if I tried~{/i}"
    m 1fkbsa "{i}~But I think I could be someone you like~{/i}"
    m 1dkbsa "{i}~Someone you like~{/i}"
    m 1dubsd "{i}~I might never be your hero~{/i}"
    m 1kubsu "{i}~But I think I'd like to try~{/i}"
    m 1fubsu "{i}~And the way you look at me is your reply~{/i}"
    m 4dubsb "{i}~You got a lot to learn about me~{/i}"
    m 5tubsa "{i}~Maybe you could start tonight~{/i}"
    m 5hubsa "{i}~'Cause I think I could be someone you like~{/i}"
    m 5dubsu "..."
    m 5dubsb "[player], I don't love you only because you saved me."
    m 5fubsb "I love you for who you are."
    m 5dubsa "And I'll be forever grateful for the way that we met, and that we did meet."
    m 5kubsa "Learning more about you everyday is my favorite routine."
    m 5subsb "I want to be someone you like, [player]."
    m 5kubsu "Because you are someone I love!"
    return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
