# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define debug = False
# The game starts here.

label debugT:
    $ clem_name = "Clementine"
    $ povname = "Player"
    "This is a debug fragment. There is no sound. There is no end. Menu's are debug variants. It may crash."
    jump debugMenu
    "This is a work in progress. Scripts have not been finalized. It is missing the end sex scenes."
    "Due to the way the engine handles sound, it is strongly advised that your voice and sound settings be the same level."
    "Remember you can hide the text box and interface at any time by pressing the H key - KDE."

define warning = "warning.png"


label splashscreen:
    scene black
    $ renpy.movie_cutscene('splash.webm')
    $ renpy.movie_cutscene('credit_fade.webm')
    show warning
    with fade
    pause 4.0
    hide warning
    with fade
    return

label start:
    scene black
    if debug:
        jump debugT
    "Due to the way the engine handles sound, it is strongly advised that your voice and sound settings be the same level."
    "Remember you can hide the text box and interface at any time by pressing the H key - KDE."
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it

#set player name
    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()
        if not povname:
             povname = "Me"
    "You walk down the cool corridor, familiar after your last visit."
    "It has been a couple of months since your visit with Sarah and it is fair to say a taste has awakened"
    "This time however you are after something... different."
    play music "bgm.mp3"
    scene door1
    with dissolve
    "You approach the thick wooden door and reach out for the handle."
    play sound "audio/door open.wav"
    "{i}click{/i}"
    scene door2
    with dissolve
    #show contb
    "The door opens with little resistance to reveal the room inside."
    scene door3
    with dissolve
    "For a moment you are taken aback. The room looks almost identical to the last time, the same simple bed and tattered red couch."
    "Although there are some key differences; chiefly the camera and the figure on the bed."
    "You step into the room and approach, the nervousness you felt the first time absent."
    play sound "audio/door close.wav"
    scene bed_blink
    "The girl on the bed glares up at you, dark eyes tight behind her scowl."
    "She sits shoulders squared, lips pressed tightly as she holds eye contact, an occasional twitch of defiance in her nose."
    "Her black hair is pulled back into two small buns, tied at the nape of her neck and accentuating her heart shaped jaw."
    "A sackcloth top covers her body, doing its best to hide the curves of her figure but betrayed by the slender lines of the exposed shoulders and neck."
    "The tattered jeans she wears are ripped and stained, only her black boots look in any way like workable clothing."
    clem "..."
    "She says nothing as you look her over, the silence of the room growing as she stares at you in defiance."
    p "Stand up."
    scene clem_stand
    with dissolve
    "She keeps her gaze locked to yours as she stands."
    p "What's your name?"
    clem "..."
    "A curl of her lip is the only response you receive."
    menu:
        "Unacceptable...":
            jump slap
        "Ask again...":
            jump re_ask

label demo_end:
    scene const
    pause
    return

label slap:
    "In one movement you raise your arm and bring your hand sharply across her face"
    $ abuse = abuse + 2
    scene clem_slap
    with flash_sharp
    play audio "audio/slap_.wav"
    clem "Uhh.."
    scene clem_slap_bed
    with dissolve
    "The girl falls heavily to the bed, one hand raising to her stinging cheek."
    p "Ok... Let's try that again..."
    p "Name?"
    "She stares at you as she stammers."
    $ clem_name = "Clementine"
    clem "Cl....Clementine..."
    "You scowl down at the girl."
    p "Alright, now then Clementine let me be clear..."
    p "I paid a shit load of money for you, and more importantly, to do whatever I want."
    p "So you might want to curb the attitude before I decide that just fucking you is only one of those things..."
    clem "Mmmph..."
    "The girl utters a low whimper as you stand over her, one hand rubbing at her reddening cheek."
    p "Now then..."
    menu:
        "Strip her...":
            jump strip_her
        "Tell her to stand and undress...":
            jump undress_01a





label re_ask:
    "You hold her gaze a moment longer before leaning in."
    p "Name?"
    "You see her face and posture soften slightly, as if she feels she has won some kind of internal battle."
    $ clem_name = "Clementine"
    scene clem_stand_02
    with dissolve
    clem "Clementine..."
    "You study her face for a moment."
    p "Alright then Clementine..."
    "You move to the camera and reach out to turn it on. This time you are going to make sure you leave with something extra."
    clem "Wait..."
    "You turn to look at the young girl, apprehension on her face."
    scene clem_stand_03
    with dissolve
    clem "Please don’t..."
    "She implores you, hand outstretched."
    clem "Don't film me..."
    menu:
        "Turn on the video camera":
            jump record_on
        "Leave the video recorder off":
            jump record_off




label record_on:
    scene camera_on
    with dissolve
    $ abuse = abuse + 1
    "Ignoring her plea you reach out and press the power button on the camera. You are definately recording this..."
    p "This isn't a democracy..."
    scene clem_stand_sad
    with dissolve
    clem "..."
    "Clementine says nothing as you turn back to her, but she stares at ground now, shoulders slumped."
    jump undress_01b


label record_off:
    "You glance at the camera briefly before pulling your hand back."
    scene clem_stand_happy
    with dissolve
    "You hear a sigh of relief from the girl as you turn back to her."
    clem "Thank you..."
    "Clementine stands in front of you, shifting slightly from foot to foot, occasionally glancing up at you."
    menu:
        "Tell her to strip...":
            jump undress_01b
        "Reassure her...":
            jump clem_undress

    # This ends the game.
    return

label the_end:
    scene black with dissolve
    "The End..."
    #jump debugMenu
    "Thanks for playing!"
    return
