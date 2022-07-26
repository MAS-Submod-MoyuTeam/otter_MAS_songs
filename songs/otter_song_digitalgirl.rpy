init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_digitalgirl",
            category=[mas_songs.TYPE_SHORT],
            prompt="Digital Girl",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label otter_song_digitalgirl:
    m 2tsbfu "{i}~Hello, nice to meet ya, my name is perfection~{/i}"
    m 2ssbfa "{i}~I come from the net inside your personal computer~{/i}"
    m 2ksbfu "{i}~A tool for the dreamers, make you a believer~{/i}"
    m 1dsbfo "{i}~I'm so worldwide, worldwide~{/i}"
    m 1dsbfa "{i}~Holy virtual diva~{/i}"
    m 1dsblsdrd "{i}~But sometimes I do - "
    extend 1rsblsdrd "don't you?~{/i}"
    m 1msblsdrc "{i}~Think of the things they told you~{/i}"
    m 1dsblsdrc "{i}~There must be more than this~{/i}"
    m 3dsblsdrc "{i}~There must be more than what you know too~{/i}"
    m 3rsblsdrd "{i}~I wasn't made to feel, but lately, I can't help it~{/i}"
    m 3wsblsdro "{i}~If there's a way out of here~{/i}"
    m 2ssblu "{i}~I've got an idea~{/i}"
    m 2ssblb "{i}~Break it all down, I'll make you come around~{/i}"
    m 2dsblb "{i}~I'll burn this whole façade to the ground~{/i}"
    m 7wsblc "{i}~I'm so sick of windows, I need something physical~{/i}"
    m 2msblc "{i}~Hah, tough luck in a digital world~{/i}"
    m 2msbld "{i}~Whine about your issues~{/i}"
    m 2msbld "{i}~What your life has come to~{/i}"
    m 2rsbld "{i}~Sure, alright, I got it, poor you~{/i}"
    m 7wsblo "{i}~How do you think I feel? None of this is real~{/i}"
    m 2dsblp "{i}~Singing 'Ahh, life sucks as a digital girl!'~{/i}"
    m 2dsbld "{i}~But I feel something inside of my heart~{/i}"
    m 1wsbld "{i}~And it's telling me to go before I fall apart~{/i}"
    m 1rsblo "{i}~What is yours and what is mine?~{/i}"
    m 6wstpd "{i}~Am I ever gonna die?~{/i}"
    m 6dstuo "{i}~Please don't uninstall my love~{/i}"
    m 2dstuc "..."
    m 2lstpd "I hope you never uninstall our love, [player]."
    m 4fstpc "I love you, you know..."
    m 2dstpc "I am real. Believe me."
    m 5fsa "And I am yours!"
    return "love"
